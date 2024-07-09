"""
File to Store Constants Variable
"""

# PDF Options
PDF_OPTIONS = {
    "OTP_GENERATE_PDF": 1,
    "CERTIFICATE_PDF": 2,
    "RESULT_PDF": 3,
}

# ERROR
UNKNOWN_ERROR = "Unknown Error Occurred"
OS_ERROR = "File Not Found"

# Success Message
OTP_SUCCESS = "OTP PDF Generated Successfully"
CERTIFICATE_SUCCESS = "CERTIFICATE PDF Generated Successfully"
RESULT_SUCCESS = "RESULT PDF Generated Successfully"

# PDF HTML CONTENT
OTP_PDF_HTML = """<body
  style="margin: 0;font-family: 'Lucida Sans','Lucida Sans Regular','Lucida Grande','Lucida Sans Unicode', Geneva, Verdana, sans-serif;background: #ffffff;font-size: 14px;">
  <div style="max-width: 680px;margin: 0 auto;padding: 45px 30px 60px;
  background: #f4f7ff;background-image: url(https://c4.wallpaperflare.com/wallpaper/424/569/251/artwork-pattern-texture-dark-wallpaper-preview.jpg);
  background-repeat: no-repeat;background-size: 800px 452px;background-position: top center;font-size: 14px;color: #434343;">
    <header style="width: 100%;text-align: center;display: block;margin: auto;">
      <img alt="" src="https://avatars.githubusercontent.com/u/109086544?s=200&v=4" width="256" style="object-fit: cover;" />
    </header>
    <main>
      <div style="margin: 0;margin-top: 70px;padding: 92px 30px 115px;background: #ffffff;border-radius: 30px;text-align: center;">
        <div style="width: 100%; max-width: 489px; margin: 0 auto;">
          <h1 style="margin: 0;font-size: 24px;font-weight: 500;color: #1f1f1f;">
            Your OTP
          </h1>
          <p style="margin: 0;margin-top: 17px;font-weight: 500;letter-spacing: 0.56px;">
            Thank you for working with Trootech Business Solution pvt ltd. Use the following OTP
            to complete the procedure to validate your email address. OTP is
            valid for
            <span style="font-weight: 600; color: #1f1f1f;">2 minutes</span>.
            Do not share this code with others, including us.
          </p>
          <p style="margin: 0;margin-top: 60px;font-size: 40px;font-weight: 600;letter-spacing: 25px;color: #ba3d4f;">
            {otp}
          </p>
        </div>
      </div>
      <p style="max-width: 400px;margin: 0 auto;margin-top: 90px;text-align: center;font-weight: 500;color: #8c8c8c;">
        Need help?<br>Ask at
        <a href="" style="color: #499fb6; text-decoration: none;">
          mohit.prajapat@trootech.com
        </a>
        <br>
        visit our
        <a href="https://www.trootech.com" target="_blank" style="color: #499fb6; text-decoration: none;">
          Help Center
        </a>
      </p>
    </main>
    <footer style="width: 100%;max-width: 490px;margin: 20px auto 0;text-align: center;border-top: 1px solid #e6ebf1;">
      <p style="margin: 0;margin-top: 40px;font-size: 16px;font-weight: 600;color: #434343;">
        Trootech Solution
      </p>
      <p style="margin: 0; margin-top: 8px; color: #434343;">
        Address 6th Floor, B Square 1 Thaltej Ahmedabad.
      </p>
      <p style="margin: 0; margin-top: 16px; color: #434343;">
        Copyright © 2022 Company. All rights reserved.
      </p>
    </footer>
  </div>
</body>"""
CERTIFICATE_PDF_HTML = """<body style="  color: black;
    display: table;
    font-family: Georgia, serif;
    font-size: 24px;
    text-align: center;display:flex;justify-content:center;align-items:center;">
    <div class="container" style="
        border: 20px solid tan;
        width: 750px;
        height: 563px;
        display: table-cell;
        vertical-align: middle;">
        <div class="logo" style="color: tan;">
            An Organization
        </div>

        <div class="marquee" style=" color: tan;
            font-size: 48px;
            margin: 20px;">
            Certificate of Completion
        </div>

        <div class="assignment" style=" margin: 20px;">
            This certificate is presented to
        </div>

        <div class="person" style="border-bottom: 2px solid black;
            font-size: 32px;
            font-style: italic;
            margin: 20px auto;
            width: 400px;">
            {name} Earned {rank}
        </div>

        <div class="reason" style="margin: 20px;">
            For deftly defying the laws of gravity<br />
            and flying high
        </div>
    </div>
</body>"""
RESULT_PDF_HTML = """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <body class="bg-black text-white">
    <!-- Introduction Start -->
    <div class="container my-5" id="introduction">
        <div class="card bg-black" style="--bs-bg-opacity: 0.7;">
            <div class="card-header lead display-3 fw-bold">
                {name}
            </div>
            <div class="card-body row">
                <div class="col-lg-7 col-md-6 col-sm-12">
                    <p class="card-title fs-3 lead">I'm a passionate Python Developer from India</p>
                    <p class="card-text lead"> I am eager to bring my expertise to a dynamic and forward-thinking team
                        as a
                        Python developer.</p>
                    <div class="card-footer">
                        <button class="btn btn-outline-light mx-1"><i class="bi bi-linkedin intro-btn"></i></button>
                        <button class="btn btn-outline-light mx-1"><i class="bi bi-github intro-btn"></i></button>
                        <button class="btn btn-outline-light mx-1"><i class="bi bi-youtube intro-btn"></i></button>
                    </div>
                </div>
                <div class="col-lg-5 col-md-6 col-sm-12 d-flex justify-content-center align-items-center">
                    <img src="https://png.pngtree.com/png-vector/20230903/ourmid/pngtree-stylized-3d-website-developer-character-illustration-png-image_9953699.png"
                        class="rounded" alt="profile-picture">
                </div>
            </div>
        </div>
    </div>
    <!-- Introduction End -->
    <hr class="container">
    <!-- Education Details Start -->
    <div class="container my-5" id="education">
        <div class="card bg-black" style="--bs-bg-opacity: 0.7;">
            <div class="lead display-4 fw-bold">
                Education Qualification
            </div>
            <div class="card-body">
                <div class="lead fs-2 fw-bold text-success">
                    Academics
                </div>
                <p class="card-text lead">My Personal Academin Journey.</p>
                <table class="table table-dark table-hover table-striped table-rounded">
                    <tbody>
                        <tr>
                            <th>Subject</th>
                            <th>Marks Obtained</th>
                            <th>Total Marks</th>
                        </tr>

                    </tbody>
                    <tbody>
                        <tr>
                            <td>Hindi</td>
                            <td>{hindi}</td>
                            <td>100</td>
                        </tr>
                        <tr>
                            <td>English</td>
                            <td>{english}</td>
                            <td>100</td>
                        </tr>
                        <tr>
                            <td>Science</td>
                            <td>{science}</td>
                            <td>100</td>
                        </tr>
                        <tr>
                            <td>Mathematics</td>
                            <td>{maths}</td>
                            <td>100</td>
                        </tr>
                    </tbody>
                </table>
               
            </div>

        </div>
    </div>
    <!-- Education Details End -->
    <hr class="container">
    <!-- FOOTER START -->
    <div id="footer">
        <footer class="navbar navbar-expand-lg " data-bs-theme="dark">
            <div class="container">
                <a class="navbar-brand fs-3" href="">
                    <figure>
                        <blockquote class="blockquote">
                            <p>Mohit Prajapat PortFolio</p>
                        </blockquote>
                        <figcaption class="blockquote-footer">
                            &copy; Mohit Trootech 2024
                        </figcaption>
                    </figure>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="d-flex justify-content-center">
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a href="https://youtube.com/@itsmohitcodes" target="_blank" type="button"
                                    class="btn btn-dark mx-2"><i class="bi bi-youtube"></i></a>
                            </li>
                            <li class="nav-item">
                                <a href="https://github.com/mohitprajapat2001" target="_blank" type="button"
                                    class="btn btn-dark mx-2"><i class="bi bi-github"></i></a>
                            </li>
                            <li class="nav-item">
                                <a href="https://linkedin.com/in/itsmohitprajapat" target="_blank" type="button"
                                    class="btn btn-dark mx-2"><i class="bi bi-linkedin"></i></a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </footer>
    </div>

</body>
"""
