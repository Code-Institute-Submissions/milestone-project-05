<!-- ![MUSIC site logo](assets/readme-assets/readme-images/logo.jpg "MUSIC site logo") -->

# "A platform to raise the profile of print designers and connect them with new customers"

# MUSIC. 

View the project on Github pages [here](https://trisdauvergne.github.io/milestone-project-02/)

## An introduction to the project

The 'MUSIC.' site offers users the chance to indulge their curiosity by searching for a musical artist or band and to preview 30 second clips of their most popular songs. The experience is clean and stripped back to allow the user to fulfill their goal easily.

The 'MUSIC.' site incorporates an API from the music streaming service 'Deezer' which hosts over 30 million tracks. The site is free for anyone to use as even though Deezer does offer a subscription service, the 'MUSIC.' site doesn't require the user to login to a Deezer account to perform the search or listen to the 30 second clips. 

## UX

### Site Users - who is the site focused on?
1. Ria, “I’m on my way to see Jax Jones tonight and want to see what his most popular songs are”.
2. Jen, “I’m on my way to karaoke and know I want to sing Britney Spears but can’t remember which songs I know. I want to see a list of songs and hear clips of the songs to jog my memory”
3. Harry, “I want to hear Bucks Fizz songs because I’m a big fan”
4. Rachael, “There’s a singer called George something who sings a really catchy song that’s stuck in my mind, but I don’t know the title of the song! I might recognise the title if I saw it but would need to search for singers called George first and hear the songs to try find out the title”

### The 'MUSIC.' site is the best place for users to achieve their goals because: 
- The site is easy to navigate with clear instructions, steps and accessibility
- The site is easily accessible without the need for login details or a subscription
- It provides users with an easy solution to finding a specific song by an artist or group 
- It allows users to easily explore an artist or group's most popular songs
- It provides users with the option to listen to a 30 second clip of all songs

# WIREFRAMES 
1. Opening page (before search):
 <!-- - [Desktop](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/desktop-wireframe-1.jpg)
 - [Tablet](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/tablet-wireframe-1.jpg)
 - [Mobile](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/mobile-wireframe-1.jpg) -->

2. Artist information (after search):
 <!-- - [Desktop](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/desktop-wireframe-2.jpg)
 - [Tablet](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/tablet-wireframe-2.jpg)
 - [Mobile](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/mobile-wireframe-2.jpg) -->

3. Song information (after an artist name is clicked):
 <!-- - [Desktop](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/desktop-wireframe-3.jpg)
 - [Tablet](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/tablet-wireframe-3.jpg)
 - [Mobile](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/mobile-wireframe-3.jpg) -->

 4. Preview songs (after a song title is clicked):
 <!-- - [Desktop](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/desktop-wireframe-4.jpg)
 - [Tablet](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/tablet-wireframe-4.jpg)
 - [Mobile](https://github.com/trisdauvergne/milestone-project-02/blob/master/assets/readme-assets/wireframes/mobile-wireframe-4.jpg) -->

## FEATURES

The site is based around a single page layout. 
The design of the site is very stripped back, with a black and white colour scheme with neon green to highlight clicked elements. 

The site opens with the **heading** 'MUSIC.' and a brief **introduction** to the site and its features. The introduction consists of two short sentences. The heading will appear in the top left hand side on desktop and tablet size screens, and top center on mobile size screens. The instruction copy will always sit below it.

The user enters the artist name into the **input box**. When the user clicks into the input box, it clears the text 'artist name here'. When the search button is clicked or the enter button pressed this box automatically clears whatever value the user has input into the box and replaces it with the original text 'artist name here'. This encourages the user to repeat the process and perform another search. If the search doesn't return any results (which could be due to incorrect spelling or the artist not being on the Deezer database), an error message will show up asking the user to try again.
Next to the input box is the **search button**, which will search for whatever the user has entered into the input box. When the search button is clicked, this clears the text the user has typed into the input box. 

When the user clicks 'search' the artist results will appear in the **artist column** to the right hand side. They will appear beneath a **header** that says 'artist' along with a **short instruction** on what to do. The search results will be filtered to only show names which include the actual name the user has searched for. The artist(s) name results will appear in a list and each of the names will be a **clickable button** which will be highlighted green when hovered over. On a screen size smaller than a tablet, the header 'artist' will appear below the search button with the artist name results appearing below this. 

If the user at this stage decides to conduct a new search, they can **type a new name** into the artist box, click 'search' and the results will be cleared.

When the user **clicks on the name** of any of the returned artists (or groups), it will call a new search for that artist's most popular songs. The popular songs will appear in a **songs column**  on the right hand side of the artist column. As with the artist column, the popular songs will appear beneath a **header** that says 'songs'. A **short instruction** will appear beneath the header to help the user experience. On a screen size smaller than a tablet, the header 'songs' will appear beneath the list of artist names, with a short instruction below that. The list of popular songs will then appear beneath this. As with the artist names, each of the song titles is a **clickable button**.

When the user **clicks on a song title**, it will make another column appear to the right hand side of the song titles. This will be the **preview column** and will contain a **header** saying 'listen' with a **short instruction** beneath it. Beneath this text, an **audio player** will have also appeared which will give the user the chance to listen to a 30 second clip of the song. The audio won't play automatically, and the user will need to press play in order to hear the song. A **now playing** text will also show up beneath the audio player, to improve the user experience and show the user which song has loaded. A small image of the **album artwork** will appear beneath the audio player. If the user clicks on a different song, the audio and image underneath will update. To maintain the ease of use, when the user scrolls down the page, the audio player and image will become **sticky** and stay in the top right hand corner of the viewport. On a screen size smaller than a tablet, the album artwork won't show and the audio player will sit at the top of the screen for an easy user experience.

### Existing features

#### Permanently on page
- **Heading** and **introduction** is always on the page as a reminder of the name of the site and what features the site offers. On a desktop these are on the left hand side, but on a tablet and smaller screen sizes these are at the top of the page above everything else.
- **Input box** is always on the page to offer the user somewhere to input an artist name and encourage searching. This always sits below the heading and introduction. Upon loading the page, the input box will have the text 'artist name here' in it to guide the user through the process. When the user clicks inside the box, this will automatically clear. When the user presses the search button, this will also clear whatever value has been input into the box.
- **Search button** is always on the page to enable the user to perform a search easily. This sits beside the input box on a desktop but beneath it on a tablet and smaller size screens. When clicked, the search button flashes with a pop of neon green to show the user that the site has registered their action.  

#### Appear on page after functions are executed
- The **artist column** appears when the user has searched for an artist name. The artist column will consist of a header, short instruction and space for artists' names. On a desktop, the column is styled to appear with a subtle left border to define a separate space from the permanent elements. The border helps the user read down the list, thus aiding accessibility. On a tablet size screen, this will sit in a row with the other columns beneath the permanent elements. On a mobile screen this will sit beneath the search button with the 'song' column beneath it. 
- The 'artist' **header** and **short instruction** will appear at the top of the artist column. The instruction will continue to guide the user through their experience on the site, prompting them to click on an artist. The instruction is styled with a subtle green bottom border to define a separate space. The instruction on a mobile size screen will differ to larger screens, instructing users that when an artist is clicked on, their songs will appear below.
- Each name returned from the user's artist search will appear within the artist column as a list of **clickable buttons**. When the user hovers over any name, it will turn neon green and the text increases in size and weight to aid accessibility and clearly show the user where they are. When the user clicks on a name it will perform a new search to return that artist's most popular songs. The artist names will always sit beneath the artist column's short instruction.
- When the user **clicks on the name** of an artist (or group), this will perform a search for that will return that artist's most popular songs in a new column on the right hand side.
- The **songs column** will appear when the user clicks on an artist name and will consist of a header, short instruction and space for that artist's most popular songs. On a desktop, the column will be styled to appear with a subtle left border across the height of the page to define a separate space and aid readability. On a tablet size screen, this will sit in a row next to the artist names column. On a mobile screen this will sit beneath the artists' names. 
- The 'songs' **header** and **short instruction** will sit at the top of this column. The short instruction will encourage the user to click on a song. For consistency, the instruction is styled with a subtle green bottom border to define a separate space. The short instruction will differ on a mobile size-screen in response to where the audio-player in the preview column will be positioned on different screen sizes. 
- Each song in the column will be a **clickable button**. When the user hovers over any song title, it will turn neon green and the text will increase in size and weight to aid accessibility.
- When the user **clicks on a song title**, it will create a new column on the right hand side of the 'songs' column
- The **preview column** will appear when a song title is clicked on and will contain an audio player and album artwork. The preview column will not appear on a mobile size screen.
- The 'preview **header** will be positioned at the top of the column. Beneath the header will be a **short instruction** to guide the user through their experience on the site. To maintain consistency, this will be styled as per the 'artist' and 'songs' column with a subtle neon green bottom border. 
- An **audio player** will appear when a song title is clicked and give users a way to listen to a clip of the selected song. The clip will not play automatically and the user will be required to press play to listen to a song. When a different song title is clicked, the audio will stop and the user will be required to press play to listen to the new song that is loaded. The audio player will appear beneath the header on a desktop and tablet, on a mobile size screen the audio player will appear at the top of the screen in the neon green bar. 
- **Album artwork** will also appear beneath the audio player when a song title is clicked. Album artwork will only be visible on a desktop and tablet size screen but not on a mobile.
- The audio player will always be **sticky** so when the user scrolls down the page it will always remain visible. 
- At any stage after a search has been performed, the user can type a new name into the input box, press the search button and this will **reset** any previous search results. The column headers will remain. 
- An **error message** will appear if the user has made a spelling mistake or the API can't return any results that match exactly what the user has searched for

### Features to implement in the future
- Feature to view music videos using data from another API
- Feature to view song lyrics using data from another API

## Technologies used
- HTML and CSS programming languages
<!-- - [BootstrapCDN](https://www.bootstrapcdn.com/): [BootStrap4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) to assist with the structuring and responsiveness of the site
- [RapidAPI](https://rapidapi.com/) for providing the Deezer SDK and access to the Deezer API
- [Deezer](https://rapidapi.com/deezerdevs/api/deezer-1) for the API and access to the song network
- [Google Fonts](https://fonts.google.com/) for the fonts used throughout the page
- [Github](https://github.com/) to store repositories of the project
- [Gitpod](https://www.gitpod.io/) for providing the workspace where the code was written
- [ICO Converter](https://www.icoconverter.com/) to create the tab icon -->

## Testing

<!-- Testing information can be found in the separate testing file which can be accessed [here](milestone-project-2-testing.md). -->

## Deployment

This project was developed using the [Gitpod](https://www.gitpod.io/) IDE, commited to Git and pushed to Github using its built in function. 

The following steps were taken to deploy this page from its [Github](https://github.com/trisdauvergne/milestone-project-04) repository to Github pages:

1. Log into [GitHub](https://github.com/)
2. Select trisdauvergne/milestone-project-02 from the list of repositories
3. Select 'Settings' from the row of menu items on screen
4. Scroll down to the 'Github Pages' section
5. Under 'Source', click the drop down menu and select 'Master Branch'
6. The page is automatically refreshed and the website is now deployed
7. The link can now be found in the same 'Github Pages' section after 'Your page is now published at...'

At the moment of submitting this Milestone project the Development Branch and Master Branch are identical.

## To run this project locally

Follow the below steps to clone this project from Github:

1. Go to the project repository [here](https://github.com/trisdauvergne/milestone-project-04)
2. Look for the green button on the right hand side of the page that says 'Clone or Download' (you may need to scroll down slightly to see it)
3. Copy and paste the link in the box
4. Open Terminal
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 2.
> git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
7. Press Enter. Your local clone will be created.

## Credits

### Content
- Copy for the site has been written by Tristan Dauvergne
- All artist and song data has called from the [Deezer API](https://rapidapi.com/deezerdevs/api/deezer-1) 

### Media
- Headphone icon in tab sourced from [Icons 8](https://icons8.com)
- [Emojipedia](https://emojipedia.org/people/) for the frowning face emoji in the error message

### Acknowledgments
This site has been built as my Milestone 2 Project to demonstrate incorporating JavaScript and an API into a site. I selected a music API for a few reasons:
1. I love music and I often think of artists who I haven't listened to for a while then want to listen to their songs
2. I know there is a lot of data connected to music but I have often found that a lot of it is not relevant to my mission 

The design inspiration from this site comes from many places including typographic posters and book layouts.

I have been guided through this project by my mentor Brian Macharia who has given me professional guidance to improve the UX of this site.