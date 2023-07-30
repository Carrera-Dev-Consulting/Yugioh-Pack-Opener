# High Level Design

At a high level we are going to be creating two seperate applications for this. We will be creating the client side rendering of the data we get on packs and opennings and we will be creating a server-side process for generating the packs/pull results. This will allow us to be able to leverage accounts created by the oauth flow using google sign on without having us do any meaningful work which will be nice because storing passwords is ass and having to create a whole new password just to use our app would be equally terrible.

![System Diagram for Whole Flow](./diagrams/Yugioh%20Card%20Drawer%20Diagram.drawio.png)


Currently we will be serving the frontend app using an Nginx server that will also serve as a proxy for the images stored on currently planned s3 so we don't have to worry about it locally but will maybe change depending on how we develop the app as well as for our backend communication.  

The web app will be talking to a backend fastapi(python framework) instance that will be scaled up as much as we feel the need to and then that will also be proxied by Nginx so we can have a single domain used for both.

We will have our database store all the card information to be able to not be limited by our sources retreival but we should consider something to keep our database updated to poll on the database maybe monthly to run a the script we had to seed the database.

We will be storing images in s3 that we pull from our datasource and storing the URI's in the database to allow the frontend application to pull them and render them.
