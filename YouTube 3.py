YT> SEARCH_VIDEOS "cat"
 Here are the results for cat: 
 1)Amazing Cats (amazing_cats_video_id) [#cat, #animal]
 2)Another Cat Video (another_cat_video_id) [#cat, #animal] 
 
YT> SEARCH_VIDEOS "cat"
 1) Amazing Cats (amazing_cats_video_id) [#cat, #animal]
 2) Another Cat Video (another_cat_video_id) [#cat, #animal]
 
YT> SEARCH_VIDEOS_WITH_TAG #cat
 Here are the results for #cat:
 1) Amazing Cats (amazing_cats_video_id) [#cat, #animal]
 2) Another Cat Video (another_cat_video_id) [#cat, #animal]
 
 YT> SEARCH_VIDEOS_WITH_TAG #blah
 No search results for #blah 
 YT> SEARCH_VIDEOS_WITH_TAG #cat
 No search results for cat 
 
 
 
 
YT> {FLAG_VIDEO} amazing_cats_video_id, dont_like_cats
 Successfully flagged video: "Amazing Cats" (reason: dont_like_cats)
 YT> {FLAG_VIDEO} Another Cat Video
 Successfully flagged video: another_cat_video_id (reason: Not Supplied)
 YT> {FLAG_VIDEO} amazing_cats_video_id
 Cannot flag video: "Video is already flagged" 
 YT> {FLAG_VIDEO} (video_does_not_exist, flag_video_reason)
 Cannot flag video: "Video does not exist" 
 YT> {PLAY} amazing_cats_video_id
 Cannot play video: "Video is currently flagged" (reason: dont_like_cats)
 YT> {PLAY} amazing_cats_video_id
 Cannot play video: "Video is currently flagged" (reason: Not supplied)
 YT> {ADD_TO_PLAYPLIST} "my_playlist" amazing_cats_video_id
 Cannot add video to my_playlist: "Video is currently flagged" (reason: dont_like_cats)
 YT> {ADD_TO_PLAYPLIST} "my_playlist" another_cat_video_id
 Cannot add video to my_playlist: "Video is currently flagged" (reason: Not Supplied)

YT> {CREATE_PLAYLIST} "my_playlist"
 Successfully created new playlist: my_playlist
 
YT> {ADD_TO_PLAYPLIST} "my_playlist" amazing_cats_video_id
 Added video to my_playlist: Amazing Cats 
 
YT> {FLAG_VIDEO} amazing_cats_video_id, dont_like_cats
 Successfully flagged video: Amazing Cats (reason: dont_like_cats)
 
YT> {ADD_TO_PLAYPLIST} "my_playlist" amazing_cats_video_id
 Cannot add video to my_playlist: Video is currently flagged (reason: dont_like_cats)

YT> {FLAG_VIDEO} amazing_cats_video_id
 Successfully flagged video: "Amazing Cats" (reason: Not supplied)
 YT> {FLAG_VIDEO} another_cat_video_id
 Successfully flagged video: Another Cat Video (reason: Not Supplied)
 YT> {FLAG_VIDEO} life_at_google_video_id
 Successfully flagged video: Life at Google (reason: Not supplied)
 YT> {FLAG_VIDEO} funny_dogs_video_id 
 Successfully flagged video: Funny Dogs (reason: Not supplied)
 YT> {FLAG_VIDEO} nothing_video_id
 Successfully flagged video: Video about nothing (reason: Not supplied)
 YT> {PLAY_RANDOM}
 No videos available 
 
YT> {FLAG_VIDEO} amazing_cats_video_id, dont_like_cats
 Successfully flagged video: "Amazing Cats" (reason: dont_like_cats)
 
YT> {SHOW_ALL_VIDEOS}
 Here's a list of all available videos:
  "Amazing Cats" (amazing_cats_video_id) [#cat, #animal] - FLAGGED (REASON: dont_like_cats)
   "Another Cat Video" (another_cat_video_id) [#cat, #animal]
   "Funny Dogs" (funny_dogs_video_id) [#dog, #animal]
   "Life at Google" (google_video_id) [#google, #career]
   "Video about nothing" (nothing_video_id) []
   
YT> {CREATE_PLAYLIST} "my_playlist"
 Successfully created new playlist: "my_playlist"
 YT> {ADD_TO_PLAYPLIST} "my_playlist" amazing_cats_video_id
 Added video to "my_playlist": "Amazing Cats"
 YT> {FLAG_VIDEO} amazing_cats_video_id, dont_like_cats
 Successfully flagged video: "Amazing Cats" (reason: dont_like_cats)
 YT> {SHOW_PLAYLIST} "my_playlist"
 Showing playlist: "my_playlist"
 "Amazing Cats" (amazing_cats_video_id) [#cat, #animal] - FLAGGED (reason: dont_like_cats)

Y> {SEARCH_VIDEOS} "cat"
 Here are the results for cat:
  1) "Amazing Cats" (amazing_cats_video_id) [#cat, #animal]
  2) Another Cat Video (another_cat_video_id) [#cat, #animal]
      Would you like to play any of the above? [1]

YT> {FLAG_VIDEO} amazing_cats_video_id dont_like_cats
 Successfully flagged video: "Amazing Cats" (reason: dont_like_cats)
 
YT> {SEARCH_VIDEO} "cat"
 Here are the results for cat: 
  1) Another Cat Video (another_cat_video_id) [#cat, #animal]
      Would you like to play any of the above? "Video does not exist"

YT> {SEARCH_VIDEOS_WITH_TAG} #cat 
 Here are the results for #cat:
  1) Another Cat Video (another_cat_video_id) [#cat, #animal]
      Would you like to play any of the above [1]

YT> {PLAY_VIDEO} amazing_cats_video_id
 Playing video: "Amazing Cats"
 YT> {SHOW_PLAYING} 
  Currently playing: "Amazing Cats" (amazing_cats_video_id) [#cat, #animal]
 YT> {FLAG_VIDEO} amazing_cats_video_id dont_like_cats
  Stopping video: "Amazing Cats"
  Successfully flagged video: "Amazing Cats" (reason: dont_like_cats)
 YT> {SHOW_PLAYING}
 "No video is currently playing"
 
YT> {FLAG_VIDEO} amazing_cats_video_id
 Successfully flagged video: "Amazing Cats" (reason: Not Supplied)
YT> {ALLOW_VIDEO} amazing_cats_video_id
 Successfully removed flag from video: "Amazing Cats" 
YT> {ALLOW_VIDEO} amazing_cats_video_id
 Cannot remove flag from video: "Video is not flagged"
YT> {ALLOW_VIDEO} non_existing_video_id
 Cannot remove flag from video: "Video does not exist"
YT> {CREATE_PLAYLIST} "my_playlist"
 Successfully created new playlist: "my_playlist"
YT> {ADD_TO_PLAYPLIST} "my_playlist" amazing_cats_video_id
 Added video to "my_playlist": "Amazing Cats"

YT> {FLAG_VIDEO} amazing_cats_video_id dont_like_cats
 Successfully flagged video: "Amazing Cats" (reason: dont_like_cats)
YT> {SHOW_PLAYLIST} "my_playlist"
 Showing playlist: "my_playlist"
 "Amazing Cats" (amazing_cats_video_id) [#cat, #animal] - FLAGGED (reason: dont_like_cats)
YT> {ALLOW_VIDEO} amazing_cats_video_id
 Successfully removed flag from video: "Amazing Cats"
YT> {SHOW_PLAYLIST} "my_playlist"
 Showing playlist: "my_playlist"
 "Amazing Cats" (amazing_cats_video_id) [#cat, #animal]


  