<h1>Use</h1>

This program downloads the top twitch.tv clips from some game. These clips are then concatenated into a single .mp4 file and then uploaded onto youtube.


<h2>Setup</h2>

This program uses the Twitch API and the Youtube Data API v3. This means that in order to run this, you must first have access to a Twitch API key and a Youtube Data API v3 OAuth 2.0 client ID. For the Youtube API, set up a OAuth 2.0 client ID with type = Other.

Once you have access to both of these, there are two files that will need to be created to run this program. In the src folder, create a file 'client_id.txt'. Copy and paste the Twitch client ID into the txt file and save. The second file is for the Youtube upload. From the Credentials page on the Youtube Data API v3, select your OAuth 2.0 client ID and press the 'DOWNLOAD JSON' button. Move this file to the src folder, and rename it to 'client_secrets.json'.

TODO: Remove clips that overlap each other in a VOD.
