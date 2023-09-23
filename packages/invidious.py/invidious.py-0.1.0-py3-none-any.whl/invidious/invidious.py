from .playlist_item import PlaylistItem
from .channel_item import ChannelItem
from .recommended_video import RecommendedVideo
from .comments_list import CommentsList
from .short_video import ShortVideo
from .video_item import VideoItem
from .comment import Comment
from .channel import Channel
from .video import Video
from .config import *

import multiprocessing
import requests

class Invidious:
    """
    Base Invidious class.
    """

    def __init__(self, 
        enable_logger: bool=True, timeout: int=5,
        mirrors: list=list(), check_best_mirror: bool=True) -> None:
        """
        :enable_logger - Enable or disable logs.
        :timeout - request wait timeout.
        :mirrors - list of mirrors you want to use.
        :check_best_mirror - use multiprocessing library for check fast responsible mirror
        """
        self.enable_logger = enable_logger
        self.timeout = timeout
        self.check_best_mirror = check_best_mirror

        if len(mirrors) == 0: self.mirrors = MIRRORS
        else: self.mirrors = mirrors

        self.manager = multiprocessing.Manager()
        self.wmirrors = self.manager.list()
        self.mprocs = list()

    def _log(self, text: str) -> None:
        if self.enable_logger:
            print(text)

    def _mirror_request(self, mirror: str) -> None:
        api_url = mirror+"/api/v1/popular"
        try: response = requests.get(api_url, headers=HEADERS, timeout=self.timeout)
        except:
            self._log(f"MirrorError: {mirror} doesn't response.")
            return

        if response.status_code == 200:
            self._log(f"INFO: Mirror {mirror} is work.")
            self.wmirrors.append(mirror)
        else:
            self._log(f"MirrorError: {mirror} doesn't response.")

    def _update_mirrors(self) -> None:
        self.wmirrors[:] = []
        for mirror in self.mirrors:
            self._mirror_request(mirror)
            if len(self.wmirrors) > 0:
                return

    def _update_mirrors_mp(self) -> None:
        self.wmirrors[:] = []
        for mirror in self.mirrors:
            process = multiprocessing.Process(target=self._mirror_request, args=(mirror,))
            self.mprocs.append(process)
            process.start()
        
        while len(self.wmirrors)==0 and len(multiprocessing.active_children())>0: pass
        
        for proc in self.mprocs:
            proc.kill()

    def _get_working_mirror(self) -> str:
        if len(self.wmirrors) == 0: 
            if self.check_best_mirror:
                self._update_mirrors_mp()
            else:
                self._update_mirrors()
        return self.wmirrors[0]

    def _request(self, url: str):
        mirror = self._get_working_mirror()
        try: response = requests.get(mirror+url, headers=HEADERS, timeout=self.timeout)
        except Exception as e:
            self._log(f"RequestError: {e}")
            return None
        if response.status_code == 200: return response.json()
        elif response.status_code == 429:
            self._log("RequestError: Too many requests.")
        elif response.status_code == 404:
            self._log("RequestError: Page not found.")

    def _edit_args(self, args: dict={}):
        argstr = ""
        index = 0
        for key, value in args.values():
            subchar = "&"
            if index == 0: subchar = "?"
            argstr += f"{subchar}{key}={value}"
            index += 1

        return argstr

    def search(self, query: str, page=0, sort_by="", duration="", date="", ctype="", feauters=[], region=""):
        """
        Invidious search method. Return list with VideoItem, ChannelItem, PlaylistItem.

        query: your search query.
        page: number of page.
        sort_by: [relevance, rating, upload_date, view_count].
        date: [hour, today, week, month, year].
        duration: [short, long].
        ctype: [video, playlist, channel, all] (default: video).
        feauters: [hd, subtitles, creative_commons, 3d, live, purchased, 4k, 360, location, hdr].
        region: ISO 3166 country code (default: US).
        """
        req = f"/api/v1/search?q={query}"
        if page > 0: req += f"&page={page}"
        if sort_by != "": req += f"&sort_by={sort_by}"
        if duration != "": req += f"&duration={duration}"
        if date != "": req += f"&date={date}"
        if ctype != "": req += f"&type={ctype}"
        if feauters != []:
            req += "&feauters="
            for feauter in feauters:
                req += feauter+","
            req = req[:len(req)-2]
        if region != "": req += f"region={region}"

        jdict = self._request(req)
        itemsList = []

        if jdict is None: return itemsList

        for item in jdict:
            citem = None
            if item['type'] == 'channel': citem = ChannelItem()
            elif item['type'] == 'video': citem = VideoItem()
            elif item['type'] == 'playlist': citem = PlaylistItem()
            if citem != None: 
                citem.from_json(item)
                itemsList.append(citem)
        
        return itemsList

    def get_comments(self, videoId: str, sort_by: str="", 
                     source: str="", continuation: str=""):
        """
        Invidious get_comments method. Return CommentsList by videoId

        sort_by: "top", "new" (default: top)
        source: "youtube", "reddit" (default: youtube)
        continuation: like next page of comments
        """
        req = f"/api/v1/comments/{videoId}"
        args = {}
        if sort_by != "": args['sort_by'] = sort_by
        if source != "": args['source'] = source
        if continuation != "": args['continuation'] = continuation
        args = self._edit_args(args)
        req += args

        response = self._request(req)
        if response == None: return None
        
        clist = CommentsList()
        clist.from_json(response)

        cmts = clist.comments
        comments = []
        for item in cmts:
            comment = Comment()
            comment.from_json(item)
            comments.append(comment)
        clist.comments = comments

        return clist

    def get_video(self, videoId: str, region=""):
        """
        Invidious get_video method. Return Video by id.
        
        videoId: id of video.
        region: ISO 3166 country code (default: US).
        """
        req = f"/api/v1/videos/{videoId}"
        if region != "": req += f"?region={region}"

        response = self._request(req)
        if response == None: return None
            
        rVideos = response['recommendedVideos']
        recommendedVideos = []
        for item in rVideos:
            vitem = RecommendedVideo()
            vitem.from_json(item)
            recommendedVideos.append(vitem)
        response['recommendedVideos'] = recommendedVideos

        video = Video()
        video.from_json(response)

        return video

    def get_channel(self, authorId: str, sort_by=""):
        """
        Invidious get_channel method. Return Channel by id.
        
        authorId: id of channel.
        sort_by: sorting channel videos. [newest, oldest, popular] (default: newest).
        """
        req = f"/api/v1/channels/{authorId}"
        if sort_by != "": req += f"?sort_by={sort_by}"

        response = self._request(req)
        if response == None: return None

        lVideos = response['latestVideos']
        latestVideos = []
        for item in lVideos:
            vitem = VideoItem()
            vitem.from_json(item)
            latestVideos.append(vitem)
        response['latestVideos'] = latestVideos

        channel = Channel()
        channel.from_json(response)

        return channel

    def get_popular(self):
        """
        Invidious get_popular method. Return list with ShortVideo.
        """
        req = f"/api/v1/popular"

        response = self._request(req)
        if response == None: return None
            
        pVideos = response
        popularVideos = []
        for item in pVideos:
            vitem = ShortVideo()
            vitem.from_json(item)
            popularVideos.append(vitem)

        return popularVideos

    def get_trending(self, type="", region=""):
        """
        Invidious get_popular method. Return list with VideoItem.

        type: [music, gaming, news, movies].
        region: ISO 3166 country code (default: US).
        """
        req = f"/api/v1/trending"
        if type != "": req += f"?type={type}"
        if region != "" and type == "": req += f"?region={region}"
        elif region != "": req += f"&region={region}"

        response = self._request(req)
        if response == None: return None
            
        tVideos = response
        trendingVideos = []
        for item in tVideos:
            vitem = VideoItem()
            vitem.from_json(item)
            trendingVideos.append(vitem)

        return trendingVideos


if __name__ == "__main__":
    iv = Invidious()
    print(iv.wmirrors)
