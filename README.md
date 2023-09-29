<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gxldcptrick/Yugioh-Pack-Opener">
    <img src="images/logo.png" alt="Logo for Repo" width="80" height="80">
  </a>

<h3 align="center">Yugioh Pack Opener</h3>

  <p align="center">
    This is a web app that enables users to be able to generate and mock pack openings for use on online drafting for yugioh.
    <br />
    <a href="https://github.com/gxldcptrick/Yugioh-Pack-Opener/tree/main/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://yugioh-pack-opener.gxldcptrick.dev">View Demo</a>
    ·
    <a href="https://github.com/gxldCptRick/Yugioh-Pack-Opener/issues/new?assignees=&labels=bug%2C+enhancement%2C+help+wanted&projects=&template=bug_report.md&title=%5BBUG%5D">Report Bug</a>
    ·
    <a href="https://github.com/gxldCptRick/Yugioh-Pack-Opener/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![YugiohPackOpener][site-screen-shot]](https://yugioh-pack-opener.gxldcptrick.dev)

This is a project is built using Fast API(python), React(js) and Flutter. We will be making the entire stack free and opensource so if you would like to host all the pieces yourself you can otherwise we will be making sure it is up and ready at [https://yugioh-pack-opener.gxldcptrick.dev](https://yugioh-pack-opener.gxldcptrick.dev)

This is actively being worked on so please feel free to open any issues or suggest ideas in our issues. We are all working fulltime so it will be a minute before we can get to everything but we will be working on it.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![React][React.js]][React-url]
[![Flutter][Flutter.dev]][Flutter-url]
[![FastAPI][FastAPI.dev]][Fast-url]
[![MySQL][MySQL.com]][MySQL-url]
[![NGinx][nginx.com]][nginx-url]
[![Docker][docker.com]][docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You will need to install dependencies for: python, node, docker to be able to fully build and run the project locally.
* yarn
  ```sh
  npm install yarn@latest -g
  ```
* python 3.10.4
  ```sh
  # using pyenv
  pyenv install 3.10.4
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/gxldcptrick/Yugioh-Pack-Opener.git
   ```
2. Use Docker Compose to build the apps for you in Docker
   ```sh
   # to run the containers without locking your terminal
   docker-compose -f docker/docker-compose.yml up -d 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can interact with the api using postman like
```
# Lists cards that are being tracked by the system.
curl --location 'https://localhost:8082/api/v1/cards'

# Lists sets that are being tracked by the system
curl --location 'https://localhost:8082/api/v1/sets/'

# Generates a Pack that you opened
curl --location 'https://localhost:8082/api/v1/packs/open/' \
--header 'Content-Type: application/json' \
--data '{
    "selections": [
        {
            "packId": "some-set-id",
            "totalDesired": 1 
        }
    ]
}'
```

_For more examples, please refer to the [Documentation](https://github.com/gxldcptrick/Yugioh-Pack-Opener/wiki)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Apache-2.0 license. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Milo - me@gxldcptrick.dev

Project Link: [https://github.com/gxldcptrick/Yugioh-Pack-Opener](https://github.com/gxldcptrick/Yugioh-Pack-Opener)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Frontend Engineer [Dean-Pesek: Dean Pesek](https://github.com/Dean-Pesek)
* Mobile Engineer [vCertxfiedGoat: Alexander Quintanilla aka The Goat](https://github.com/vCertxfiedGoat)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/gxldcptrick/Yugioh-Pack-Opener.svg?style=for-the-badge
[contributors-url]: https://github.com/gxldcptrick/Yugioh-Pack-Opener/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gxldcptrick/Yugioh-Pack-Opener.svg?style=for-the-badge
[forks-url]: https://github.com/gxldcptrick/Yugioh-Pack-Opener/network/members
[stars-shield]: https://img.shields.io/github/stars/gxldcptrick/Yugioh-Pack-Opener.svg?style=for-the-badge
[stars-url]: https://github.com/gxldcptrick/Yugioh-Pack-Opener/stargazers
[issues-shield]: https://img.shields.io/github/issues/gxldcptrick/Yugioh-Pack-Opener.svg?style=for-the-badge&color=%23c001af
[issues-url]: https://github.com/gxldcptrick/Yugioh-Pack-Opener/issues
[license-shield]: https://img.shields.io/github/license/gxldcptrick/Yugioh-Pack-Opener.svg?style=for-the-badge
[license-url]: https://github.com/gxldcptrick/Yugioh-Pack-Opener/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Flutter.dev]: https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white
[Flutter-url]: https://flutter.dev/
[FastAPI.dev]: https://img.shields.io/badge/fastapi-000000?style=for-the-badge&logo=fastapi&logoColor=white 
[Fast-url]: https://fastapi.tiangolo.com/
[nginx.com]: https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white
[nginx-url]: https://www.nginx.com/
[MySQL.com]: https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://www.mysql.com/
[screen-shot-url]: images/screenshot.jpg
[docker.com]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
