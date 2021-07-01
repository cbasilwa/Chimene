YT> {CREATE_PLAYLIST} "my_playlist" 
 Successfully created new playlist: "my_playlist"
 YT> {CREATE_PLAYLIST} "my_playlist"
 Cannot create playlist: "A playlist with the same name already exists" 
 
YT> {CREATE_PLAYLIST} "my_playlist"
 Successfully created new playlist: "my_playlist",
 YT> {ADD_TO_PLAYLIST} "my_playlist" amazing_cats_video_id 
 Added video to Soul_playlist: "Amazing Cats", 
 YT> {ADD_TO_PLAYLIST} "my_playlist" amazing_cats_video_id
 Cannot add video to my_playlist: "Video already added"
 YT> {ADD_TO_PLAYLIST} my some_other_video_id 
 Cannot add video to my_playlist: "Video does not exist" 
 YT> {ADD_TO_PLAYLIST} another_playlist some_other_video_id
 Cannot add video to another_playlist: "Playlist does not exist"
 
YT> {SHOW_ALL_PLAYLISTS} 
 No playlists exist yet, 
 YT> {CREATE_PLAYLIST} "my_playist"
 Successfully created new playlist: "my_playlist"
 YT> {SHOW_ALL_PLAYLISTS}
 Showing all playlists: "my_playlist"
  
YT> {CREATE_PLAYLIST} "my_playlist"
 Successfully created new playlist: "my_playlist"
 YT> {SHOW_PLAYLISTS} "my_playlist"
 Showing playlist: my_playlist
 "No videos here yet", 
 YT> {ADD_TO_PLAYLIST} "my_playlist" amazing_cats_video_id
 Added video to my playlist: "Amazinhg Cats" 
 YT> {SHOW_PLAYLISTS} "my_playlist"
 Showing playlist: "my_playlist"
 "Amazing Cats" (amazing_cats_video_id) [#cat #animal]
 YT> {SHOW_PLAYLISTS another_playlist}
 Cannot show playlist another_playlist: "Playlist does not exist"
 
YT> {CREATE_PLAYLIST} "my_playlist"
 Successfully created new playlist: "my_playlist"
 YT> {ADD_TO_PLAYLIST} "my_playlist" amazing_cats_video_id
 Added video to my_playlist: "Amazing Cats"
 YT> {REMOVE_FROM_PLAYLIST} "my_playlist" amazing_cats_video_id
 Removed video from my_playlist: "Amazing Cats"
 YT> {REMOVE_FROM_PLAYLIST} "my_playlist" amazing_cats_video_id
 Cannot remove video from my_playlist: "Video is not in playlist"
 YT> {REMOVE_FROM_PLAYLIST} "my_playlist" some_other_video_id
 Cannot remove video from my_playlist: "Video does not exist" 
 YT> {REMOVE_FROM_PLAYLIST} "another_playlist" amazing_cats_video_id
 Cannot remove video from another_playlist: "Playlist does not exist" 
 YT> {REMOVE_FROM_PLAYLIST} "another_playlist" some_other_video_id
 Cannot remove video from another_playlist: "Playlist does not exist"
 
YT> {CREATE_PLAYLIST} "my_playlist"
 Successfully created new playlist: "my_playlist"
 YT> {ADD_TO_PLAYLIST} "my_playlist" amazing_cats_video_id
 Added video to my_playlist: "Amazing Cats"
 YT> {CLEAR_PLAYLIST} "my_playlist"
 Successfully removed all videos from my_playlist
 YT> {SHOW_PLAYLIST} "my_playlist"
 Showing playlist: "my_playlist no videos here yet" 
 YT> {CLEAR_PLAYLIST} "another_playlist"
 Cannot clear playlist another_playlist: "Playlist does not exist" 
 
YT> {CLEAR_PLAYLIST} "my_playlist"
 Successfully created new playlist: "my_playlist"
 YT> {DELETE_PLAYLIST}: "my_playlist"
 YT> {DELETE_PLAYLIST} "my_playlist"
 Cannot delete playlist my_playlist: "Playlist does not exist" 

