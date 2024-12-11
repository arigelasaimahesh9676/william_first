Hello USA

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awesome Nginx Docker Web Page</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e3f2fd; /* Light blue background */
            color: #333;
        }

        header {
            background-color: #0288d1; /* Darker blue for header */
            color: white;
            padding: 20px 0;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }

        nav {
            background-color: #1976d2; /* Blue for navigation */
            padding: 10px;
            text-align: center;
        }

        nav a {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            display: inline-block;
            transition: background 0.3s ease;
        }

        nav a:hover {
            background-color: #1565c0; /* Darker blue on hover */
        }

        .container {
            width: 90%;
            margin: auto;
            overflow: hidden;
            padding: 20px;
        }

        .section {
            background: white;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }

        .features {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
        }

        .feature {
            flex-basis: 30%;
            background-color: #bbdefb; /* Light blue for feature boxes */
            padding: 20px;
            text-align: center;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease-in-out;
        }

        .feature:hover {
            transform: translateY(-10px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .gallery {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }

        .gallery img {
            flex-basis: 30%;
            max-width: 30%;
            margin-bottom: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .testimonial {
            background-color: #0288d1; /* Matching testimonial background */
            color: white;
            padding: 20px;
            border-radius: 5px;
        }

        .testimonial h3 {
            margin-top: 0;
        }

        footer {
            background-color: #1976d2; /* Matching footer background */
OBOBOBOBOBOBOBOBOBOBOB            color: white;
            text-align: center;
OBOBOBOBOBOBOBOBOBOBOB            padding: 10px;
            position: relative;
            width: 100%;
            bottom: 0;
        }

        .contact-form {
            display: flex;
            flex-direction: column;
OBOBOBOBOBOBOBOBOBOBOB        }

        .contact-form input, .contact-form textarea {
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        .contact-form input[type="submit"] {
            background-color: #0288d1; /* Submit button color */
            color: white;
            cursor: pointer;
            border: none;
        }
OBOBOBOBOBOBOBOBOBOBOB
        .contact-form input[type="submit"]:hover {
OBOBOBOBOBOBOBOBOBOBOB            background-color: #03a9f4; /* Lighter blue on hover */
        }

        @media (max-width: 768px) {
OBOBOBOBOBOBOBOBOBOBOB            .features, .gallery {
OBOBOBOBOBOBOBOBOBOBOB                flex-direction: column;
                align-items: center;
            }

            .feature, .gallery img {
                flex-basis: 100%;
                max-width: 100%;
            }
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to the Awesome Nginx Docker Page</h1>
</header>

<nav>
    <a href="#about">About</a>
    <a href="#features">Features</a>
    <a href="#gallery">Gallery</a>
    <a href="#testimonials">Testimonials</a>
OBOBOBOBOBOBOBOBOBOBOB    <a href="#contact">Contact Us</a>
</nav>
OBOBOBOBOBOBOBOBOBOBOB
OBOBOBOBOBOBOBOBOBOBOB<div class="container">
OBOBOBOBOBOBOBOBOBOBOB
    <section id="about" class="section">
OBOBOBOBOBOBOBOBOBOBOB        <h2>About This Project</h2>
        <p>This is a dynamic web page running on an Nginx server inside a Docker container. It demonstrates how to deploy and run a containerized web application with rich features and a responsive design. Docker makes application deployment scalable and reliable.</p>
    </section>

    <section id="features" class="section">
        <h2>Features</h2>
        <div class="features">
            <div class="feature">
                <h3>Fast & Lightweight</h3>
                <p>Using the lightweight Nginx server with Alpine Linux, this web application is efficient and fast.</p>
            </div>
            <div class="feature">
                <h3>Dockerized</h3>
                <p>This application is fully containerized, making it portable, scalable, and easy to deploy anywhere.</p>
            </div>
            <div class="feature">
                <h3>Responsive Design</h3>
                <p>The web page is fully responsive, adapting to mobile, tablet, and desktop screens.</p>
            </div>
            <div class="feature">
                <h3>Zero Downtime Deployment</h3>
                <p>Update your application seamlessly without interrupting the user experience.</p>
            </div>
            <div class="feature">
                <h3>Multi-Environment Support</h3>
                <p>Run this web app in development, testing, and production environments effortlessly using Docker Compose.</p>
            </div>
            <div class="feature">
                <h3>Scalable Architecture</h3>
OBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOB[6~OBOBOBOBOBOBOBOB                <p>Easily scale your application horizontally with Docker for consistent performance as your traffic grows.</p>
            </div>
OBOBOBOBOBOBOBOBOBOBOB            <div class="feature">
                <h3>CI/CD Integration</h3>
                <p>Integrate seamlessly with Continuous Integration/Continuous Deployment pipelines for automated builds and deployments.</p>
            </div>
            <div class="feature">
                <h3>Secure by Design</h3>
                <p>Isolated containers and well-defined boundaries ensure the application is secure and easy to maintain.</p>
            </div>
            <div class="feature">
                <h3>Cloud-Ready</h3>
                <p>Deploy this Dockerized web application on any cloud platform with minimal configuration.</p>
OBOBOBOBOBOBOBOBOBOBOB            </div>
        </div>
OBOBOBOBOBOBOBOBOBOBOB    </section>
OBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOB
    <section id="gallery" class="section">
        <h2>Gallery</h2>
        <div class="gallery">
            <img src="https://via.placeholder.com/600x400" alt="Sample Image 1">
            <img src="https://via.placeholder.com/600x400" alt="Sample Image 2">
            <img src="https://via.placeholder.com/600x400" alt="Sample Image 3">
        </div>
    </section>

OBOBOBOBOBOBOBOBOBOBOB    <section id="testimonials" class="section testimonial">
[6~OBOBOBOBOBOBOBOB        <h2>What People Say</h2>
        <h3>John Doe</h3>
        <p>"This is by far the best Dockerized application I have worked with. The deployment was seamless, and it performed flawlessly."</p>
        <h3>Jane Smith</h3>
        <p>"The clean design and fast performance make this application stand out. Plus, Docker makes it so easy to manage and scale."</p>
    </section>

    <section id="contact" class="section">
        <h2>Contact Us</h2>
        <form class="contact-form" action="#" method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <input type="submit" value="Send Message">
[5~OAOAOAOAOAOAOAOA        </form>
OAOAOAOAOAOAOAOAOAOAOA    </section>
OAOAOAOAOAOAOAOAOAOAOA
</div>

<footer>
    <p>&copy; 2024 Awesome Nginx Docker Example</p>
</footer>

</body>
</html>
added
