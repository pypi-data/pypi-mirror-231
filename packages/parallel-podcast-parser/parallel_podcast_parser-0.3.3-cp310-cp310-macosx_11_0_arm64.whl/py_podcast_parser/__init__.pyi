from typing import List

async def parse_single_podcast(
    url: str, allow_exceptions: bool, request_timeout: int
) -> PodcastFromRss:
    """
    Parses a single podcast from the given url.
    :param url: The url to the podcast rss feed.
    :param allow_exceptions: If true, throw an exception if there is an error. If false, return None in case of error.
    :param request_timeout: The timeout in seconds for the http request. Standard timeout is ~30 seconds.
    """

async def parse_list_of_podcasts(
    urls: List[str], verbose: bool, request_timeout: int
) -> List[PodcastFromRss]:
    """
    Fetch and parse list of rss feeds in parallel.
    Returns a list of [PodcastFromRss]. Indexes of the returned list correspond to indexes of the input urls list. If there is an error, the corresponding item is None.

    To access properties of the a retuned object (PodcastFromRss), call `get_` method. Example:
    ```python
    shows = await py_podcast_parser.parse_list_of_podcasts(
        urls=urls[0:10000], verbose=True, request_timeout=30
    )
    for show in shows:
        print(show.get_title())
        print(show.get_language())
        ...

        episodes = show.get_episodes()

        for episode in episodes:
            print(episode.get_title())
            print(episode.get_description())
            ...
    ```

    :param urls: List of urls to the podcast rss feeds.
    :param verbose: If true, print the error messages.
    :param request_timeout: The timeout in seconds for the http request. Standard timeout is ~30 seconds.
    """

class PodcastFromRss(object):
    def get_title(self) -> str:
        """Get the title of the Podcast Show."""
        ...
    def get_description(self) -> str:
        """Description of the show. It may have HTML elements in it."""
        ...
    def get_language(self) -> str:
        """Language of the podcast"""
        ...
    def get_author(self) -> str:
        """The author / company / creator of the podcast"""
        ...
    def get_image_url(self) -> str:
        """Image URL for the show. Each episode may have its own image."""
        ...
    def get_category(self) -> str:
        """Global category. If more than 1 category is present, the first is taken"""
        ...
    def get_guid(self) -> str:
        """Global Unique Identifier of the podcast. This is NOT the same as the episode guid."""
        ...
    def get_link(self) -> str:
        """A link to website / homepage of the show / creator."""
        ...
    def get_explicit(self) -> str:
        """Get if the show as a whole (hence all its episodes) is marked with `explicit`."""
        ...
    def get_episodes(self) -> List[EpisodeFromRss]:
        """Get list of references to the episodes. You can loop over the list via native Python `for`, `map`, etc. loop.
        To access property of episode, use the getter method again.

        Example:
        ```python
        episodes = show.get_episodes()
        for episode in episodes:
            print(episode.get_title())
            print(episode.get_description())
            ...
        ```
        """
        ...

class EpisodeFromRss(object):
    def get_title(self) -> str:
        """Get the title of the episode."""
        ...
    def get_enclosure(self) -> str:
        """Link to the audio file of the episode.
        Many podcasters use URL prefixes to track downloads.
        You can be redirected multiple times before getting the actual audio file."""
        ...
    def get_enclosure_type(self) -> str:
        """The MIME type of the audio file.
        Example: `audio/mpeg` for mp3.
        Itunes allow only flac, wav and mp3 files."""
        ...
    def get_description(self) -> str:
        """Description of the episode. It may have HTML elements in it."""
        ...
    def get_pub_date(self) -> int:
        """Publication date of the episode as Unix timestamp.
        Milliseconds since 1970-01-01 00:00:00 UTC."""
        ...
    def get_duration(self) -> int:
        """Duration of the episode in seconds."""
        ...
    def get_guid(self) -> str:
        """Unique identifier of the episode. This is NOT the same as the podcast guid.
        It should be unique globally, but not guaranteed."""
        ...
    def get_explicit(self) -> bool:
        """Get if the episode is marked with `explicit`."""
        ...
    def get_image_url(self) -> str:
        """Image URL for the episode. Some podcasters use the same image for all episodes, others use unique image for some / every episode."""
        ...
