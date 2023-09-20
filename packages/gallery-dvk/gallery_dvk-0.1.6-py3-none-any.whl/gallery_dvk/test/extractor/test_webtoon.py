#!/usr/bin/env python3

import os
import metadata_magic.file_tools as mm_file_tools
from gallery_dvk.extractor.webtoon import Webtoon
from os.path import abspath, basename, exists, join

def test_match_url():
    """
    Tests the match_url method.
    """
    with Webtoon([]) as webtoon:
        # Test getting a toon url
        match = webtoon.match_url("https://www.webtoons.com/en/romance/Blades-of-Furry/list?title_no=2383/")
        assert match["section"] == "en/romance/blades-of-furry/list?title_no=2383"
        assert match["type"] == "toon"
        match = webtoon.match_url("http://www.webtoons.com/en/romance/blades-of-furry/list?title_no=2383&page=6/")
        assert match["section"] == "en/romance/blades-of-furry/list?title_no=2383"
        assert match["type"] == "toon"
        match = webtoon.match_url("WebToons.com/es/comedy/manual-para-no-morir/list?title_no=5068")
        assert match["section"] == "es/comedy/manual-para-no-morir/list?title_no=5068"
        assert match["type"] == "toon"
        match = webtoon.match_url("www.webtoons.com/es/comedy/Manual-para-no-morir/list?title_no=5068&page=4")
        assert match["section"] == "es/comedy/manual-para-no-morir/list?title_no=5068"
        assert match["type"] == "toon"
        # Test getting an episode url
        match = webtoon.match_url("https://www.webtoons.com/es/comedy/manual-para-no-morir/ep-44/viewer?title_no=5068&episode_no=44/")
        assert match["section"] == "es/comedy/manual-para-no-morir/ep-44/viewer?title_no=5068&episode_no=44"
        assert match["type"] == "episode"
        match = webtoon.match_url("http://www.webtoons.com/es/comedy/manual-para-no-morir/ep-44/viewer?title_no=5068&episode_no=32")
        assert match["section"] == "es/comedy/manual-para-no-morir/ep-44/viewer?title_no=5068&episode_no=32"
        assert match["type"] == "episode"
        match = webtoon.match_url("webtoons.com/en/romance/blades-of-furry/ep-9-medium-rare/viewer?title_no=2383&episode_no=9")
        assert match["section"] == "en/romance/blades-of-furry/ep-9-medium-rare/viewer?title_no=2383&episode_no=9"
        assert match["type"] == "episode"
        match = webtoon.match_url("www.webtoons.com/en/romance/blades-of-furry/ep-11-empty-rink/viewer?title_no=2383&episode_no=11")
        assert match["section"] == "en/romance/blades-of-furry/ep-11-empty-rink/viewer?title_no=2383&episode_no=11"
        assert match["type"] == "episode"

def test_get_id():
    """
    Tests the get_id_method.
    """
    with Webtoon([]) as webtoon:
        index = webtoon.get_id("https://www.webtoons.com/en/comedy/swolemates/episode-1/viewer?title_no=5112&episode_no=1")
        assert index == "webtoon-en-t5112-e1"
        index = webtoon.get_id("webtoons.com/en/romance/blades-of-furry/ep-14-apology/viewer?title_no=2383&episode_no=14/")
        assert index == "webtoon-en-t2383-e14"
        index = webtoon.get_id("www.webtoons.com/es/comedy/manual-para-no-morir/ep-44/viewer?title_no=5068&episode_no=44/")
        assert index == "webtoon-es-t5068-e44"

def test_get_episodes():
    """
    Tests the get_episodes method.
    """
    with Webtoon([]) as webtoon:
        # Test getting episodes for a webtoon comic
        episodes = webtoon.get_episodes("en/comedy/swolemates/list?title_no=5112")
        assert len(episodes) > 19
        assert episodes[0]["webtoon"] == "Swolemates"
        assert episodes[0]["genre"] == "Comedy"
        assert episodes[0]["authors"] == ["LummyPix"]
        assert episodes[0]["webtoon_views"] > 8500000
        assert episodes[0]["webtoon_views"] < 9000000
        assert episodes[0]["webtoon_subscribers"] > 364000
        assert episodes[0]["webtoon_subscribers"] < 390000
        assert episodes[0]["webtoon_rating"] > 9.5
        assert episodes[0]["webtoon_rating"] < 9.9
        assert episodes[0]["webtoon_summary"].startswith("When the cocky, social-media star Braydin, and the nerdy,")
        assert episodes[0]["webtoon_summary"].endswith("than they initially thought. Also they get buff AF.")
        assert episodes[0]["title"] == "Episode 1"
        assert episodes[0]["episode"] == 1
        assert episodes[0]["date"] == "2023-05-12"
        assert episodes[0]["likes"] > 79000
        assert episodes[0]["likes"] < 81000
        assert episodes[0]["url"] == "https://www.webtoons.com/en/comedy/swolemates/episode-1/viewer?title_no=5112&episode_no=1"
        # Test getting episodes with unique titles
        episodes = webtoon.get_episodes("en/romance/blades-of-furry/list?title_no=2383")
        assert len(episodes) > 61
        assert episodes[0]["webtoon"] == "Blades of Furry"
        assert episodes[0]["genre"] == "Romance"
        assert episodes[0]["authors"] == ["Deya Muniz", "Emily Erdos"]
        assert episodes[0]["webtoon_views"] > 34000000
        assert episodes[0]["webtoon_views"] < 40000000
        assert episodes[0]["webtoon_subscribers"] > 490000
        assert episodes[0]["webtoon_subscribers"] < 500000
        assert episodes[0]["webtoon_rating"] == 9.56
        assert episodes[0]["webtoon_summary"].startswith("Emile is an up-and-coming skater in the")
        assert episodes[0]["webtoon_summary"].endswith("into something more...?")
        assert episodes[0]["title"] == "Ep. 1 - Last Minute Matchup"
        assert episodes[0]["episode"] == 1
        assert episodes[0]["date"] == "2020-12-19"
        assert episodes[0]["likes"] > 77500
        assert episodes[0]["likes"] < 79500
        assert episodes[0]["url"] == "https://www.webtoons.com/en/romance/blades-of-furry/ep-1-last-minute-matchup/viewer?title_no=2383&episode_no=1"
        assert episodes[4]["title"] == "Ep. 5 - Tiny Rival"
        assert episodes[4]["episode"] == 5
        assert episodes[4]["date"] == "2021-01-02"
        assert episodes[4]["likes"] > 69500
        assert episodes[4]["likes"] < 71000
        assert episodes[4]["url"] == "https://www.webtoons.com/en/romance/blades-of-furry/ep-5-tiny-rival/viewer?title_no=2383&episode_no=5"

def test_get_episode_info():
    """
    Tests the get_episode_info method.
    """
    with Webtoon([]) as webtoon:
        # Test getting episode with existing comic info
        episode_info = {"url":"https://www.webtoons.com/en/romance/blades-of-furry/ep-1-last-minute-matchup/viewer?title_no=2383&episode_no=1"}
        episode_info["title"] = "Episode 01"
        pages = webtoon.get_episode_info("en/romance/blades-of-furry/ep-1-last-minute-matchup/viewer?title_no=2383&episode_no=1", episode_info)
        assert len(pages) == 57
        assert pages[0]["title"] == "Episode 01"
        assert pages[0]["url"] == "https://www.webtoons.com/en/romance/blades-of-furry/ep-1-last-minute-matchup/viewer?title_no=2383&episode_no=1"
        assert pages[0]["image_url"] == "https://webtoon-phinf.pstatic.net/20201215_23/1607986880350l3WlD_JPEG/1607986880287238318.jpg?type=q90"
        assert pages[0]["image_number"] == 1
        assert pages[0]["id"] == "en-t2383-e1-1"
        assert pages[1]["image_url"] == "https://webtoon-phinf.pstatic.net/20201215_226/1607986880365HMsv0_JPEG/1607986880318238319.jpg?type=q90"
        assert pages[1]["image_number"] == 2
        assert pages[1]["id"] == "en-t2383-e1-2"
        assert pages[2]["image_url"] == "https://webtoon-phinf.pstatic.net/20201215_71/16079868809535jqiC_JPEG/1607986880904238314.jpg?type=q90"
        assert pages[2]["image_number"] == 3
        assert pages[2]["id"] == "en-t2383-e1-3"
        assert pages[56]["image_url"] == "https://webtoon-phinf.pstatic.net/20201215_118/1607986917312T3lnG_JPEG/1607986917268238310.jpg?type=q90"
        assert pages[56]["image_number"] == 57
        assert pages[56]["id"] == "en-t2383-e1-57"
        # Test getting episode while getting comic info
        pages = webtoon.get_episode_info("en/comedy/swolemates/episode-2/viewer?title_no=5112&episode_no=2")
        assert len(pages) == 60
        assert pages[0]["webtoon"] == "Swolemates"
        assert pages[0]["genre"] == "Comedy"
        assert pages[0]["authors"] == ["LummyPix"]
        assert pages[0]["webtoon_summary"].startswith("When the cocky, social-media star Braydin, and the nerdy,")
        assert pages[0]["webtoon_summary"].endswith("than they initially thought. Also they get buff AF.")
        assert pages[0]["title"] == "Episode 2"
        assert pages[0]["episode"] == 2
        assert pages[0]["date"] == "2023-05-12"
        assert pages[0]["url"] == "https://www.webtoons.com/en/comedy/swolemates/episode-2/viewer?title_no=5112&episode_no=2"
        assert pages[0]["title"] == "Episode 2"
        assert pages[0]["image_number"] == 1
        assert pages[0]["image_url"] == "https://webtoon-phinf.pstatic.net/20230506_23/1683306754067HLk8k_PNG/16833067540524479_acov1.png?type=opti"
        assert pages[0]["id"] == "en-t5112-e2-1"
        assert pages[1]["title"] == "Episode 2"
        assert pages[1]["image_number"] == 2
        assert pages[1]["id"] == "en-t5112-e2-2"
        assert pages[1]["image_url"] == "https://webtoon-phinf.pstatic.net/20230506_10/1683306754286hOcwI_PNG/16833067542741201_US_SWOLEMATES_S1_EP0002_001.png?type=opti"
        assert pages[2]["title"] == "Episode 2"
        assert pages[2]["id"] == "en-t5112-e2-3"
        assert pages[2]["image_number"] == 3
        assert pages[2]["image_url"] == "https://webtoon-phinf.pstatic.net/20230506_8/1683306754391p2nXT_PNG/16833067543598767_US_SWOLEMATES_S1_EP0002_002.png?type=opti"
        assert pages[59]["title"] == "Episode 2"
        assert pages[59]["id"] == "en-t5112-e2-60"
        assert pages[59]["image_number"] == 60
        assert pages[59]["image_url"] == "https://webtoon-phinf.pstatic.net/20230506_18/1683306753498trgbE_PNG/16833067534946490_US_SWOLEMATES_S1_EP0002_059.png?type=opti"

def test_download_page():
    """
    Tests the download_page method.
    """
    # Test if ID is already in the database
    temp_dir = mm_file_tools.get_temp_dir()
    config_file = abspath(join(temp_dir, "config.json"))
    archive_file = abspath(join(temp_dir, "webtoon.db"))
    config = {"webtoon":{"archive":archive_file, "metadata":True}}
    mm_file_tools.write_json_file(config_file, config)
    with Webtoon([config_file]) as webtoon:
        webtoon.initialize()
        json = {"title":"BoF Episode 1"}
        json["webtoon"] = "Blades of Furry"
        json["url"] = "https://www.webtoons.com/en/romance/blades-of-furry/ep-1-last-minute-matchup/viewer?title_no=2383&episode_no=1"
        json["image_number"] = 5
        webtoon.add_to_archive("webtoon-en-t2383-e1-i5")
        media_file = webtoon.download_page(json, temp_dir)
        assert media_file is None
    files = sorted(os.listdir(temp_dir)) == ["config.json", "webtoon.db"]
    # Test if file has not been written
    with Webtoon([config_file]) as webtoon:
        json["id"] = "en-t2383-e1-1"
        json["image_number"] = 1
        json["image_url"] = "https://webtoon-phinf.pstatic.net/20201215_23/1607986880350l3WlD_JPEG/1607986880287238318.jpg?type=q90"
        json["date"] = "2020-01-01"
        media_file = webtoon.download_page(json, temp_dir)
        assert basename(media_file) == "en-t2383-e1-1_BoF Episode 1.jpg"
        assert exists(media_file)
    parent_folder = abspath(join(temp_dir, "Webtoon"))
    comic_folder = abspath(join(parent_folder, "Blades of Furry"))
    episode_folder = abspath(join(comic_folder, "BoF Episode 1"))
    assert exists(episode_folder)
    json_file = abspath(join(episode_folder, "en-t2383-e1-1_BoF Episode 1.json"))
    assert exists(json_file)
    meta = mm_file_tools.read_json_file(json_file)
    assert meta["title"] == "BoF Episode 1"
    assert meta["url"] == "https://www.webtoons.com/en/romance/blades-of-furry/ep-1-last-minute-matchup/viewer?title_no=2383&episode_no=1"
    assert meta["image_url"] == "https://webtoon-phinf.pstatic.net/20201215_23/1607986880350l3WlD_JPEG/1607986880287238318.jpg?type=q90"
    assert meta["date"] == "2020-01-01"
    assert meta["webtoon"] == "Blades of Furry"
    assert meta["image_number"] == 1
    assert os.stat(media_file).st_size == 101003
    # Test that ID has been written to the database
    with Webtoon([config_file]) as webtoon:
        webtoon.initialize()
        assert webtoon.archive_contains("webtoon-en-t2383-e1-i1")
        assert webtoon.archive_contains("webtoon-en-t2383-e1-i5")
        assert not webtoon.archive_contains("webtoon-en-t2383-e1-i6")