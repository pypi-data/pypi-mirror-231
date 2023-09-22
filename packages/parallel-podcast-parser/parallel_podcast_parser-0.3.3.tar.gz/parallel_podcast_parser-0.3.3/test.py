import py_podcast_parser
import asyncio


async def exception_modes():
    # throw exception if there is an error
    try:
        result = await py_podcast_parser.parse_single_podcast(
            "https://norcalsportshop.podbean.com/feed.xml", True
        )
    except Exception as e:
        print(e)

    # fail silently and return None
    result = await py_podcast_parser.parse_single_podcast(
        "https://norcalsportshop.podbean.com/feed.xml", False, 30
    )


async def main():
    # show = await py_podcast_parser.parse_single_podcast(
    #     "https://lexfridman.com/feed/podcast/", True
    # )

    # for episode in show.get_episodes():
    #     print(episode.get_image_url())

    with open("feedUrls.txt", "r") as f:
        urls = f.read().split("\n")

    shows = await py_podcast_parser.parse_list_of_podcasts(
        urls=urls[0:400], verbose=False, request_timeout=60
    )

    print(shows)

    num_none = 0
    for show in shows:
        if show is None:
            num_none += 1
            continue

    print(f"num_none: {num_none}")


if __name__ == "__main__":
    asyncio.run(main())
