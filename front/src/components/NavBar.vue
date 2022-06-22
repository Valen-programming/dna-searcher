<template>
  <div class="nav-bar">
      <div class="logo">
          <img id="header-img" src="@/assets/img/logo.png" alt="adn searcher logo" @click="$router.push('/')"/>
      </div>
      <input id="toggle" type="checkbox">
      <label for="toggle" class="hamburger">
        <div class="top-bun"></div>
        <div class="meat"></div>
        <div class="bottom-bun"></div>
      </label>
     <div class="nav">
        <nav>
          <div class="nav-wrapper">
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
        </nav>
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
    // methods:{
    //   myFunction(){
    //     let x = document.getElementById("nav-wrapper");
    //     if (x.style.display === "block") {
    //       x.style.display = "none";
    //     } else {
    //       x.style.display = "block";
    //     }
    //   }
    // }
    
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
#toggle {
  display: none;

}
.hamburger {
  position: absolute;
  top: 5em;
  right: 5%;
  margin-left: -2em;
  margin-top: -45px;
  width: 2em;
  height: 45px;
  z-index: 5;
  display:none;
}

.hamburger div {
  position: relative;
  width: 3em;
  height: 7px;
  border-radius: 3px;
  background-color: white;
  margin-top: 8px;
  border:black solid 1.5px;
  cursor:pointer;
  display:none;
}
.nav-wrapper{
  display:flex;
  flex-direction: row;
  background-color: rgba(240, 248, 255, 0.838);
  border-radius:3px;
}
.nav-wrapper .nav-link{
  margin:5px;
  padding:15px;
  font-size:100%;
  border-radius: 3px;
  
}
.nav-wrapper .nav-link:hover {
  background-color: rgba(255, 255, 255, 0.841);
  transition: background-color 0.8s;
  box-shadow: 0px 0px 5px rgb(118, 133, 207);
}

@media(max-width:750px){
  .hamburger {
    display:block;
  }
  .hamburger div {
    display:block;
  }
  .nav {
    position: fixed;
    width: 70%;
    height: 40%;
    background-color: #090E6B;
    top: 0;
    right: 0;
    overflow: hidden;
    transition: all 0.3s ease-in-out;
    transform: scale(0);
    z-index: 4;
  }
  .nav-wrapper {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    overflow-y: auto;
    height: 100%;
  }
  .nav-wrapper .nav-link:hover {
    background-color: rgba(255, 255, 255, 0.841);
    transition: background-color 0.8s;
    box-shadow: 0px 0px 5px rgb(118, 133, 207);
}
  nav {
    text-align: left;
    margin-left: 10%;
  }
  nav-link {
    position: relative;
    text-decoration: none;
    color: #6ecddd;
    font-size: 1.2em;
    display: inline-block;
    margin-top: 1.25em;
    transition: color 0.2s ease-in-out;
    letter-spacing: 1px;
  }
}


#toggle:checked + .hamburger + .nav {
  top: 0;
  transform: scale(1);
  
}

</style>