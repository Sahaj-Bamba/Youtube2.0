<?php
session_start();

?>


<!DOCTYPE html>
<html>

<head>
	<link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">

  <title>YouTube</title>

  <!-- Bootstrap CSS CDN -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
  <!-- Our Custom CSS -->
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" type="text/css" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
  <!-- Font Awesome JS -->
  <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/solid.js" integrity="sha384-tzzSw1/Vo+0N5UhStP3bvwWPq+uvzCMfrN1fEFe+xBmv1C/AtVX5K0uZtmcHitFZ" crossorigin="anonymous"></script>
  <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/fontawesome.js" integrity="sha384-6OIrr52G08NpOFSZdxxz1xdNSndlD4vdcf/q2myIUVO0VsqaGHJsB0RaBE01VTOY" crossorigin="anonymous"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
  <script src="https://kit.fontawesome.com/yourcode.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <style type="text/css">
  @import url('https://fonts.googleapis.com/css?family=Kodchasan');
  *{
   outline: none !important;
 }
 body
 {
  font-family: 'Kodchasan', sans-serif;
  scroll-behavior: smooth;
  background: #fafafa;
}
p 
{
  /*font-family: 'Poppins', sans-serif;*/
  font-size: 1.1em;
  font-weight: 300;
  line-height: 1.7em;
  color: #999;
}
a, a:hover, a:focus 
{
 color: inherit;
 text-decoration: none;
 transition: all 0.3s;
}

.wrapper 
{
  display: flex;
  width: 100%;
  align-items: stretch;
}
#sidebar 
{
 position: fixed;
 top: 4%;
 min-width: 250px;
 max-width: 250px;
 min-height: 100vh;
 background: #7386D5;
 color: #fff;
 transition: all 0.3s;
 padding-bottom: 0px;
 padding-top: 0px;
}
#sidebar .sidebar-header 
{
 padding: 20px;
 background: #6d7fcc;
}
#sidebar.active 
{
 margin-left: -250px;
}
a[data-toggle="collapse"] 
{
 position: relative;
}

.dropdown-toggle::after 
{
 display: block;
 position: absolute;
 top: 50%;
 right: 20px;
 transform: translateY(-50%);
}
/*for smaller screens*/
@media (max-width: 768px) 
{
 #sidebar 
 {
  margin-left: -250px;
}
#sidebar.active 
{
  margin-left: 0;
}
}

#sidebar ul.components {
  padding: 20px 0;
  border-bottom: 1px solid #47748b;
}

#sidebar ul p {
  color: #fff;
  padding: 10px;
}

#sidebar ul li a {
  padding: 10px;
  font-size: 1.1em;
  display: block;
}
#sidebar ul li a:hover {
  color: #7386D5;
  background: #fff;
}

#sidebar ul li.active > a, a[aria-expanded="true"] {
  color: #fff;
  background: #6d7fcc;
}
ul ul a {
  font-size: 0.9em !important;
  padding-left: 30px !important;
  background: #6d7fcc;
}
.aaa
{
 position: absolute;
 right: 40%;
 top: 0%;
}

.mynav
{
 background: white;
 z-index: 99999;
 height: 20%;
 box-shadow: 10px 10px 5px #aaaaaa;
 position: relative,fixed;
 top: 0%;
 /*padding-bottom: 0px;*/
}


.toggler-btn
{
  border: 2px solid #d3325f;
  padding: 5px;
  transition: all 2s ease;
}

.bar
{
  width: 30px;
  height: 3px;
  margin: 5px;
  background: #d3325f ;
  transition: all 0.5s ease;
}

.change .bar1
{
  transform: rotate(-45deg) translate(-5px,6px);
}
.change .bar2
{
  opacity: 0;
}
.change .bar3
{
  transform: rotate(45deg) translate(-5px,-8px);
}

.marginmy
{
 position: absolute;
 right: 10%;
 top: 0%;	
}
.nav-link
{
 /*padding-left: 6px;*/
 color: #242424;
 text-decoration: none;
 transition: all 2s ease;
 font-size: 15px;
}
.nav-link:hover
{
  color: #d3325f;
}

.clink
{
 color: black;
}

.mycard1
{
 position: absolute;
 top: 20%;
 left: -42.5%;
 /*padding-right: 5px;*/
}

.mycard2
{
 position: absolute;
 top: 20%;
 left: 38%;
 /*padding-right: 5px;*/
}

.mycard3
{
 position: absolute;
 top: 20%;
 left: 119%;
 /*padding-right: 5px;*/
}

.mycard4
{
 position: absolute;
 top: 20%;
 left: 202%;
}

.mycard5
{
 position: absolute;
 top: 90%;
 left: 260%;
 /*padding-right: 5px;*/
}

.mycard6
{
 position: absolute;
 top: 90%;
 left: 1280%;
 /*padding-right: 5px;*/
}

.mycard7
{
 position: absolute;
 top: 90%;
 left: 2300%;
 /*padding-right: 5px;*/
}

.mycard8
{
 position: absolute;
 top: 90%;
 left: 3350%;
}

    /*#content
    {
    	position: fixed;
      }*/





    </style>

    <script type="text/javascript">
    	$(document).ready(function () {

        $('#sidebarCollapse').on('click', function () {
          $('#sidebar').toggleClass('active');
        });

      });
    </script>

  </head>

  <body>
   <div id="content">
     <nav class="navbar navbar-expand-lg navbar-light mynav">
      <div class="collapse navbar-collapse">

        <button type="button" id="sidebarCollapse" class="btn btn-info">
          <i class="fas fa-align-left"></i>
          <span>Utilities</span>
        </button>

        <b style="font-size: 20px;">YouTube</b>

        <form class="form-inline my-2 my-lg-0 aaa">
         <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
         <button class="btn btn-primary btn-md btn-lg my-2 " type="submit">Search</button>
       </form>

       <!-- labels st-->
       <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#myNavbar">
        <div class="toggler-btn">
          <div class="bar bar1"></div>
          <div class="bar bar2"></div>
          <div class="bar bar3"></div>



        </div>



      </button>
      <!--links-->
      <div class="collapse navbar-collapse" id="myNavbar">
        <ul class="navbar-nav marginmy">
         <!-- <li class="nav-item">
            <a href="#about" class="nav-link text-capitalize">Upload Vedio</a> 
        </li>
         <li class="nav-item">
            <a href="#" class="nav-link text-capitalize">Go Live</a> 
        </li>
         <li class="nav-item">
            <a href="#" class="nav-link text-capitalize">Messages</a> 
          </li> -->
          <!-- <li class="nav-item"> -->
            <!-- <a href="#" class="nav-link text-capitalize">Notifications</a>  -->
            <!-- </li> -->
            <li class="nav-item dropdown" style="position: relative; left: 0%;">
             <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              a
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
             <a class="dropdown-item" href="#">Go Live</a>
             <a class="dropdown-item" href="#">Upload Vedio</a>
             <div class="dropdown-divider"></div>
             <a class="dropdown-item" href="#">Notifications</a>
           </div>
         </li>&nbsp;&nbsp;&nbsp;&nbsp;
         <?php
        // session_start();
         if(!isset($_SESSION['name']))
         {
        	// echo "hello";
          ?>
          <li class="nav-item">
            <a href="log.php" class="nav-link text-capitalize">Sign In</a> 
          </li>
          <?php
        }
        else
        {
        	// session_start();
        	echo "<br><br><br><br>";
        	echo "&nbsp&nbsp&nbsp&nbsp<b style='font-size:20px;'>Hello, ".$_SESSION['name']."</b>&nbsp&nbsp&nbsp";
        }  
        ?>
        <?php
        if(isset($_SESSION['name']))
        {
        	?>
          <li class="nav-item dropdown" style="position: relative; left: 0%;">
           <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Profile
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
           <a class="dropdown-item" href="#">Profile</a>
           <a class="dropdown-item" href="logout.php">Logout</a>
           <!-- <div class="dropdown-divider"></div> -->
           <!-- <a class="dropdown-item" href="#">Something else here</a> -->
         </div>
       </li>
       <?php
     }

     ?>

   </ul>




 </div>
 <!-- labels en -->

</div>

</nav>
</div>

<!-- main content starts -->

<section class="main py-5">
  <div class="container">
   <div class="row">
    <div class="col-lg-4 py-5 mx-auto col-md-3 col-sm-1">


     <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Vedio title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>

    <div class="col-lg-4 py-5 mx-auto col-sm-1 col-md-3">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Vedio title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>


  <div class="col-lg-4 py-5 mx-auto col-sm-1 col-md-3">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Vedio title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>

  <div class="col-lg-4 py-5 mx-auto col-sm-1 col-md-3">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Vedio title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>

  <div class="col-lg-4 py-5 mx-auto col-sm-1 col-md-3">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Vedio title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>

  <div class="col-lg-4 py-5 mx-auto col-sm-1 col-md-3">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Vedio title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>

   


  </div>
</div>

<!-- <div class="row" style="position: absolute; top: 80%;">
  <div class="col-4">

   <div class="col-9 col-sm-6 col-lg-4 mx-auto my-4">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>

   <div class="col-9 col-sm-6 col-lg-4 mx-auto my-4">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>

    <div class="col-9 col-sm-6 col-lg-4 mx-auto my-4">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div>


   <div class="col-9 col-sm-6 col-lg-4 mx-auto my-4">
    <div class="card text-white bg-dark" style="width:  30rem; display: table;">
      <img src="https://images.pexels.com/photos/620337/pexels-photo-620337.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <ul class="list-group list-group-flush">
          <a href="#"><li class="list-group-item clink">Watch</li></a>
          <a href="#"><li class="list-group-item clink">Save to playlist</li></a>
          <a href="#"><li class="list-group-item clink">Not interested</li></a>
        </ul>
      </div>
    </div>
  </div> -->







</section>

<!-- main content ends -->





<div class="wrapper">




  <!-- Sidebar -->
  <nav id="sidebar">
    <div class="sidebar-header">
      <h3>Utilities</h3>
    </div>

    <ul class="list-unstyled components">
      <!-- <p>Dummy Heading</p> -->
      <li class="active">
        <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Home</a>
        <ul class="collapse list-unstyled" id="homeSubmenu">
          <li>
            <a href="#">Home</a>
          </li>
          <li>
            <a href="#">Trending</a>
          </li>
          <li>
            <a href="#">Subscriptions</a>
          </li>
        </ul>
      </li>
          <!--   <li>
                <a href="#">Library</a>
              </li> -->
              <li>
                <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Library</a>
                <ul class="collapse list-unstyled" id="pageSubmenu">
                  <li>
                    <a href="#">History</a>
                  </li>
                  <li>
                    <a href="#">Watch Later</a>
                  </li>
                  <li>
                    <a href="#">Liked Vedios</a>
                  </li>
                </ul>
              </li>
              <li>
                <a href="#">Portfolio</a>
              </li>
              <li>
                <a href="#">Contact</a>
              </li>
              <?php
              if(!isset($_SESSION['name']))
              {
                ?>
                <li>
                 <i class="fas fa-hand-point-down icons" aria-hidden="true" style="font-size: 40px; padding-left: 10px;"></i>
                 <div><a href="log.php">Sign in</a> to like videos, comment, and subscribe.</div>
               </li>
               <?php
             }
             ?>
           </ul>
         </nav>

       </div>

       <!-- sidebar ends -->
    <!-- <section class="main">
    	 <div class="container-fluid">
    	 	<div class="row">
    	 		<div class=" col-sm-6 col-lg-4 mx-auto my-4">
    	 		<div class="card" style="width: 18rem;">
                <img src="https://marketplace.canva.com/MADE1T8EShI/1/screen_2x/canva-stacking-social-media-apps-in-virtual-reality-MADE1T8EShI.png" class="card-img-top">
                <div class="card-body">
                  <h5 class="card-title">Card title</h5>
                  <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                  <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
              </div>
             </div>
    	 	</div>


    	 </div>







      </section> -->




      <!-- sidebar toggler -->
    <!-- <div id="content">
     <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">

            <button type="button" id="sidebarCollapse" class="btn btn-info">
                <i class="fas fa-align-left"></i>
                <span>Toggle Sidebar</span>
            </button>

        </div>
     </nav>
   </div> -->
   <!-- jQuery CDN - Slim version (=without AJAX) -->
  

 </body>

 </html>