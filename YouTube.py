YT> NUMBER_OF_VIDEOS
 [5] videos in the library 

YT> SHOW_ALL_VIDEOS 
  "Amazing cats" (amazing_cats_video_id) [#cat, #animal]
  "Another Cat Video" (another_cat_video_id) [#cat, #animal]
  "Funny Dogs" (funny_dogs_video_id) [#dog, #animal]
  "Life at Google" (life_at_google_video_id) [#google, #career]
  "Video about nothing" (nothing_vieo_id) []
 
YT> {PLAY funny_dogs_video_id}
 Stopping video: "Amazing Cats",
 Playing video: "Funny Dogs", 
 YT> PLAY funny_dogs_video_id
 Stopping video: "Funny Dogs",
 Playing video: "Amazing Cats",   
 YT> PLAY some_other_video_id 
 Cannot play video: "Video does not exist" 
 
YT> {PLAY amazing_cats_video_id}
 Playing video: "Amazing Cats",
 YT> {STOP}
 Stopping video: "Amazing Cats",
 YT> {STOP}
 Cannot stop video: "No video is currently playing" 
 
YT> {PLAY_RANDOM} 
 Playing video: "Life at Google",  
 YT> {PLAY_RANDOM}
 Stopping video: "Life at Google", 
 Playing video: "Funny Dogs", 
 Cannot play video: "No videos available"
 
YT> {PLAY amazing_cats_video_id}
 Playing video: "Amazing Cats", 
 YT> {PAUSE} 
 Pausing video: "Amazing Cats", 
 YT> {PAUSE} 
 Video already paused: "Amazing Cats", 
 YT> {STOP}
 Stopping video: "Amazing Cats", 
 YT> {PAUSE} 
 Cannot pause video: "No video is currently playing" 

YT> {PLAY amazing_cats_video_id}
 Playing video: "Amazing Cats", 
 YT> {PAUSE} 
 Pausing video: "Amazing Cats", 
 YT> {PLAY} another_cat_video_id
 Stopping video: "Amazing Cats", 
 Playing video: "Another Cat Video" 
  
YT> {PLAY amazing_cats_video_id}
 Playing video: "Amazing Cats", 
 YT> {CONTINUE} 
 Cannot continue video: "Video is not paused",
 YT> {PAUSE} 
 Pausing video: "Amazing Cats", 
 YT> {CONTINUE} 
 Continuing video: "Amazing Cats", 
 YT> {CONTINUE} 
 Cannot continue video: "Video is not paused", 
 YT> {STOP} 
 Stopping video: "Amazing Cats", 
 YT> {CONTINUE} 
 Cannot continue video: "No video is currently playing" 
 
YT> {PLAY amazing_cats_video_id}
 Playing video: "Amazing Cats" 
 YT> {SHOW_PLAYING} 
 Currently playing: Amazing Cats (amazing_cats_video_id) [#cat #animal]
 YT> {PAUSE} 
 Pausing video: "Amazing Cats" 
 YT> {SHOW_PLAYING}
 Currently playing: "Amazing Cats" (amazing_cats_video_id) [#cat #animal] - PAUSED 
 YT> [STOP} 
 Stopping video: "Amazing Cats" 
 YT> {SHOW_PLAYING}
 "No video is currently playing" 
 

  
