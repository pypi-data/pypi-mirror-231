use std::time::Duration;

use chrono::{DateTime, NaiveTime, Utc};
use dateparser::parse_with;
use pyo3::{pyclass, pymethods, IntoPy, Py, PyAny, Python};
use reqwest;
use roxmltree::Document;

use crate::parse_duration::parse_to_seconds;

#[derive(Debug, Clone)]
#[pyclass]
pub struct PodcastFromRss {
    pub title: Option<String>,
    pub description: Option<String>,
    pub language: Option<String>,
    pub author: Option<String>,
    pub image_url: Option<String>,
    pub category: Option<String>,
    pub episodes: Vec<EpisodeFromRss>,
    pub guid: Option<String>,
    pub link: Option<String>,
    pub explicit: Option<bool>,
}

impl PodcastFromRss {
    pub fn new() -> Self {
        PodcastFromRss {
            title: None,
            description: None,
            language: None,
            author: None,
            image_url: None,
            category: None,
            episodes: vec![],
            guid: None,
            link: None,
            explicit: None,
        }
    }

    pub fn set_attrs(
        &mut self,
        title: Option<String>,
        description: Option<String>,
        language: Option<String>,
        author: Option<String>,
        image_url: Option<String>,
        category: Option<String>,
        guid: Option<String>,
        link: Option<String>,
        explicit: Option<bool>,
    ) -> &mut Self {
        self.title = title;
        self.description = description;
        self.language = language;
        self.author = author;
        self.image_url = image_url;
        self.category = category;
        self.guid = guid;
        self.link = link;
        self.explicit = explicit;
        self
    }

    pub fn add_episode(&mut self, episode: EpisodeFromRss) -> &mut Self {
        self.episodes.push(episode);
        self
    }
}

#[pymethods]
impl PodcastFromRss {
    pub fn get_title(&self) -> Option<String> {
        self.title.clone()
    }

    pub fn get_description(&self) -> Option<String> {
        self.description.clone()
    }

    pub fn get_language(&self) -> Option<String> {
        self.language.clone()
    }

    pub fn get_author(&self) -> Option<String> {
        self.author.clone()
    }

    pub fn get_image_url(&self) -> Option<String> {
        self.image_url.clone()
    }

    pub fn get_category(&self) -> Option<String> {
        self.category.clone()
    }

    pub fn get_guid(&self) -> Option<String> {
        self.guid.clone()
    }

    pub fn get_link(&self) -> Option<String> {
        self.link.clone()
    }

    pub fn get_explicit(&self) -> Option<bool> {
        self.explicit.clone()
    }

    pub fn get_episodes(&self, py: Python) -> Py<pyo3::PyAny> {
        let episodes = self.episodes.clone();
        episodes.into_py(py)
    }
}

#[derive(Debug, Clone)]
#[pyclass]
pub struct EpisodeFromRss {
    pub title: Option<String>,
    pub enclosure: Option<String>,
    pub enclosure_type: Option<String>,
    pub description: Option<String>,
    pub pub_date: Option<DateTime<Utc>>,
    pub duration: Option<u32>,
    pub guid: Option<String>,
    pub explicit: Option<bool>,
    pub image_url: Option<String>,
}
impl EpisodeFromRss {
    pub fn new(
        title: Option<String>,
        enclosure: Option<String>,
        enclosure_type: Option<String>,
        description: Option<String>,
        pub_date: Option<DateTime<Utc>>,
        duration: Option<u32>,
        guid: Option<String>,
        explicit: Option<bool>,
        image_url: Option<String>,
    ) -> Self {
        EpisodeFromRss {
            title,
            enclosure,
            enclosure_type,
            description,
            pub_date,
            duration,
            guid,
            explicit,
            image_url,
        }
    }
}
#[pymethods]
impl EpisodeFromRss {
    pub fn get_title(&self) -> Option<String> {
        self.title.clone()
    }

    pub fn get_enclosure(&self) -> Option<String> {
        self.enclosure.clone()
    }

    pub fn get_enclosure_type(&self) -> Option<String> {
        self.enclosure_type.clone()
    }

    pub fn get_description(&self) -> Option<String> {
        self.description.clone()
    }

    pub fn get_pub_date(&self) -> Option<i64> {
        if self.pub_date.is_some() {
            return Some(self.pub_date.unwrap().timestamp_millis());
        }

        None
    }

    pub fn get_duration(&self) -> Option<u32> {
        self.duration.clone()
    }

    pub fn get_guid(&self) -> Option<String> {
        self.guid.clone()
    }

    pub fn get_explicit(&self) -> Option<bool> {
        self.explicit.clone()
    }

    pub fn get_image_url(&self) -> Option<String> {
        self.image_url.clone()
    }
}

#[derive(Debug)]
pub enum PodcastError {
    // The request could not be sent
    RequestSendingError(String),

    // The request reponse could not be parsed as text
    ResponseParsingError(String),

    // The text response could not be parsed as XML
    XMLParsingError(String),

    // A critical attribute is missing (ex. title)
    InvalidPodcast(String),

    // Status code different than 200 was returned (ex. 404)
    HTTPError(String),
}

pub async fn fetch(url: &String, timeout: &u64) -> Result<String, PodcastError> {
    let client = reqwest::Client::builder()
        .timeout(Duration::from_secs(*timeout))
        .build();

    let client = match client {
        Ok(client) => client,
        Err(e) => {
            return Err(PodcastError::RequestSendingError(e.to_string()));
        }
    };
    // Make a GET request
    let res = client.get(url).send().await;

    let res = match res {
        Ok(res) => res,
        Err(e) => {
            return Err(PodcastError::RequestSendingError(e.to_string()));
        }
    };

    if res.status().is_success() {
        let text = res.text().await;

        let text = match text {
            Ok(text) => text,
            Err(e) => {
                return Err(PodcastError::ResponseParsingError(e.to_string()));
            }
        };

        return Ok(text);
    } else {
        let message = format!(
            "Failed to get the XML, status of the response: {} for URL: {}",
            res.status(),
            url
        );
        return Err(PodcastError::HTTPError(message));
    }
}

pub fn parse(text: &String) -> Result<PodcastFromRss, PodcastError> {
    // Parse the XML response
    let doc = Document::parse(&text);

    let doc = match doc {
        Ok(doc) => doc,
        Err(e) => {
            return Err(PodcastError::XMLParsingError(e.to_string()));
        }
    };

    // Create a new podcast
    let mut podcast = PodcastFromRss::new();

    // Iterate over XML nodes
    for node in doc.descendants() {
        // Parse the channel
        if node.is_element() && node.tag_name().name() == "channel" {
            let title = parse_contents("title", &node);
            if title == None {
                // Break, the podcast cannot have empty title
                return Err(PodcastError::InvalidPodcast(
                    "Title not available".to_string(),
                ));
            }

            let description: Option<String> = parse_contents("description", &node);

            let language = parse_contents("language", &node);

            let author = parse_contents("author", &node);

            let image_url = parse_image(&node);

            let category = parse_category(&node);

            let category = match category {
                // Category is available
                Some(category) => Some(category),

                None => {
                    // Try to parse the category from iTunes
                    let category_itunes = parse_category_itunes(&node);

                    match category_itunes {
                        Some(category_itunes) => Some(category_itunes.to_string()),

                        // itunes or plain category is not available
                        None => None,
                    }
                }
            };

            let guid = parse_guid(&node);

            let link = parse_contents("link", &node);

            let explicit = parse_contents("explicit", &node);

            let explicit = match explicit {
                Some(explicit) => {
                    if explicit == "yes" || explicit == "Yes" || explicit == "true" {
                        Some(true)
                    } else {
                        Some(false)
                    }
                }
                None => None,
            };

            // Set the attributes of the podcast
            podcast.set_attrs(
                title,
                description,
                language,
                author,
                image_url,
                category,
                guid,
                link,
                explicit,
            );
        }

        // Parse the episodes
        if node.is_element() && node.tag_name().name() == "item" {
            // Get the title of a episode
            let title: Option<String> = parse_contents("title", &node);

            // Parse the enclosure
            let enclosure = parse_enclosure(&node);

            // Parse the enclosure type
            let enclosure_type = parse_enclosure_type(&node);

            // Get the description of a episode
            let description = parse_contents("description", &node);

            // Get the pubDate of a episode
            let pub_date = parse_contents("pubDate", &node);

            let pub_date = match pub_date {
                Some(pub_date) => {
                    let parsed_date = parse_with(&pub_date, &Utc, NaiveTime::from_hms(0, 0, 0));

                    // Try to parse the date
                    match parsed_date {
                        Ok(parsed_date) => Some(parsed_date),
                        Err(_) => None,
                    }
                }
                None => None,
            };

            // Get the duration of a episode
            let duration = parse_contents("duration", &node);

            // Parse to seconds
            let duration = match duration {
                Some(duration) => parse_to_seconds(&duration),
                None => None,
            };

            // Get the guid of a episode
            let guid = parse_guid(&node);

            let explicit = parse_contents("explicit", &node);

            let explicit = match explicit {
                Some(explicit) => {
                    if explicit == "yes" || explicit == "Yes" || explicit == "true" {
                        Some(true)
                    } else {
                        Some(false)
                    }
                }
                None => None,
            };

            let image_url = parse_image(&node);

            // Create the episode
            let episode = EpisodeFromRss::new(
                title,
                enclosure,
                enclosure_type,
                description,
                pub_date,
                duration,
                guid,
                explicit,
                image_url,
            );

            // Add the episode to the podcast
            podcast.add_episode(episode);
        }
    }

    return Ok(podcast);
}

fn parse_enclosure(node: &roxmltree::Node) -> Option<String> {
    let target_node = node
        .descendants()
        .find(|n| n.tag_name().name() == "enclosure");

    if let Some(target_node) = target_node {
        let url = target_node.attribute("url");

        // Get the value of the url
        return match url {
            Some(url) => Some(url.to_string()),
            None => None,
        };
    } else {
        None
    }
}

fn parse_image(node: &roxmltree::Node) -> Option<String> {
    let target_node = node.descendants().find(|n| n.tag_name().name() == "image");

    if let Some(target_node) = target_node {
        let attribute_elem = target_node.attribute("href");
        let tag_elem = target_node
            .children()
            .find(|n| n.tag_name().name() == "url");

        if attribute_elem.is_some() {
            return Some(attribute_elem.unwrap().to_string());
        } else if tag_elem.is_some() {
            if tag_elem.unwrap().text().is_some() {
                return Some(tag_elem.unwrap().text().unwrap().to_string());
            } else {
                return None;
            }
        }
    }

    None
}

fn parse_category_itunes(node: &roxmltree::Node) -> Option<String> {
    let target_node = node
        .descendants()
        .find(|n| n.tag_name().name() == "category");

    if let Some(target_node) = target_node {
        let category_element = target_node.attribute("text");

        return match category_element {
            Some(category_element) => Some(category_element.to_string()),
            None => None,
        };
    }

    None
}

fn parse_category(node: &roxmltree::Node) -> Option<String> {
    let target_node = node
        .descendants()
        .find(|n| n.tag_name().name() == "category");

    if let Some(target_node) = target_node {
        let category_element = target_node.text();

        return match category_element {
            Some(category_element) => Some(category_element.to_string()),
            None => None,
        };
    }

    None
}

fn parse_contents(element: &str, node: &roxmltree::Node) -> Option<String> {
    // Get the description of a episode
    let target_node: Vec<_> = node
        .descendants()
        .filter(|n| n.tag_name().name() == element)
        .collect();

    for node in target_node {
        let target_node_text: Option<&str> = node.text();

        if let Some(target_element_content) = target_node_text {
            return Some(String::from(target_element_content));
        }
    }

    None
}

fn parse_guid(node: &roxmltree::Node) -> Option<String> {
    let target_node = node
        .descendants()
        .find(|n| n.tag_name().name() == "guid" || n.tag_name().name() == "podcast:guid");

    if let Some(target_node) = target_node {
        let guid_element = target_node.text();

        return match guid_element {
            Some(guid_element) => Some(guid_element.to_string()),
            None => None,
        };
    }

    None
}
fn parse_enclosure_type(node: &roxmltree::Node) -> Option<String> {
    let target_node = node
        .descendants()
        .find(|n| n.tag_name().name() == "enclosure");

    if let Some(target_node) = target_node {
        let enclosure_type = target_node.attribute("type");

        return match enclosure_type {
            Some(enclosure_type) => Some(enclosure_type.to_string()),
            None => None,
        };
    }

    None
}
