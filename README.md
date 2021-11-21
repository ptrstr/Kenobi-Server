# [Kenobi-Server](https://aayush9029.github.io/KenobiSite/)
WIP Opensource desktop application for Kenobi. 

[![CodeQL](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/codeql-analysis.yml) [![pylint](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pylint.yml/badge.svg)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pylint.yml)

---
Download the apple watch app to get started.

<a href="https://apps.apple.com/us/app/kenobi/id1595469125"><img src="https://raw.githubusercontent.com/Aayush9029/Kenobi-Server/main/readme-assets/download-appstore-icon.png" width="150px"></a>

![Apple watch image with kenobi app running](https://aayush9029.github.io/KenobiSite/img/mainresize.png)

---

### What is [this repo?](https://github.com/Aayush9029/Kenobi-Server)
It's repo for the opensource version of kenobi desktop app which works on windows, linux along side macOS.

### Why is the desktop app opensource?
To help others who are struggling with writing code that commnunicates with between *desktop <=> iOS Devices*
> It is not limited to iOS devices (can be expanded to PWA, android apps and even desktop apps)


### How does this work?
> Websockets! 
> Desktop Application acts as a websocket server which is then connected to via client.
>
> The client then sends commands to the server and the server acts upon it.
>

### Features
  - Media Playback
    - Increase / Decrease volume
    - Pause / Play media
    - Forward / Rewind media
    - Toggle Mute
    - Exit full screen
    
  - Keyboard control
    - Up arrow
    - Down arrow
    - Right arrow
    - Left arrow
    - Space
    - Return (Enter) key
    - TAB
    
  - Trackpad Support
    - Move the cursor on the desktop by simply interacting with watch Screen.
   
  - Ping Desktop
    - Play a ping noise
    - Say "Hello There! General Kenobi!"
    - Rickroll: [Plays This beauty](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
   
  - Power options
    - Log out
    - Sleep
    - Restart
    - Power off
   
  - Launch apps
    - MACOS
      - FaceTime, Messages, Mail, Music, Notes, Safari, System Pref, Apple TV, Youtube
    - Windows / Linux
      - TBD
   

> The opensource desktop app is CLI based for now keeping it's resource usage as minimum as possible.

---

### Future of Kenobi
> Kenobi iOS and iPadOS app will be launched in upcoming months
> 
> Kenobi watchOS app will be opensourced along side their iOS counter parts in the upcoming months.
> 
> Expect more opensource and transparency!!!
