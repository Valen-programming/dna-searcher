<template>
  <div class="nav-bar">
     <div class="logo">
          <img id="header-img" src="@/assets/img/logo.png" alt="adn searcher logo" @click="$router.push('/')"/>
      </div>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <div class="nav">
        <a href="#home" class="active">..</a>

          <div id="myLinks">

            <router-link to="/">
              <div class="nav-link">Home</div> 
            </router-link>
            
            <router-link to="/alignments">
              <div class="nav-link">Alinear</div>
            </router-link>

            <router-link to="/sequences/add">
              <div class="nav-link">Añadir nueva secuencia</div>
            </router-link>

            <router-link to="/categories">
              <div class="nav-link">Catálogo de secuencias</div>
            </router-link>
      </div>
        <a href="javascript:void(0);" class="icon" @click="myFunction()">
          <i class="fa fa-bars"></i>
        </a>
    </div>

  </div>
</template>

<script>

  export default {
    name: 'NavBar',
    data(){
      return {
      }
    },
    methods:{
      myFunction(){
        let x = document.getElementById("myLinks");
        if (x.style.display === "block") {
          x.style.display = "none";
        } else {
          x.style.display = "block";
        }
      }
    }
    
  }
</script>

<style scoped>
.nav-bar {
  position: relative;
  top: 0;
  min-height: 75px;
  padding: 0px auto;
  display: flex;
  justify-content:space-between;
  align-items: center;
  margin:0px 10px;
}
.logo > img {
  max-width: 80px;
  margin: 7px;
  width:100%;
  border-radius: 10px;
}
#header-img:hover{
  transition: background-color 0.8s;
  box-shadow: 2px 2px 5px rgb(243, 244, 250);
  padding: white;
  cursor: pointer;
}
#myLinks{
  display:flex;
  flex-direction: row;
  background-color: rgba(240, 248, 255, 0.838);
  border-radius:3px;
}
#myLinks .nav-link{
  margin:5px;
  padding:15px;
  font-size:100%;
  border-radius: 3px;
  
}
#myLinks .nav-link:hover {
  background-color: rgba(255, 255, 255, 0.841);
  transition: background-color 0.8s;
  box-shadow: 0px 0px 5px rgb(118, 133, 207);
}
.nav a.icon{
  display:none;
}
@media(max-width:800px){
  .nav {
    overflow: hidden;
    background-color: rgb(70, 133, 161);
    position: relative;
  }
  .nav #myLinks {
    display: none;
  }
  .nav .nav-link {
    color: white;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
    display: block;
  }
  .nav a.icon {
    background: rgb(0, 0, 0);
    display: block;
    position: absolute;
    right: 3px;
    top: 2px;
  }
  .nav .nav-link:hover {
    background-color: #ddd;
    color: black;
  }
  .active {
    background-color: rgb(70, 133, 161);
    color: white;
  }
}

</style>