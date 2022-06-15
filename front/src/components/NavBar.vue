<template>
  <div class="nav-bar">
     <div class="logo">
          <img id="header-img" src="@/assets/img/logo.png" alt="adn searcher logo" @click="$router.push('/')"/>
      </div>
      <div class="nav">
        
        <router-link to="/">
          <div class="nav-link">Home</div> 
        </router-link>
       
        <router-link to="/about_us">
          <div class="nav-link">Sobre nosotros</div>  
        </router-link>
        
        <router-link to="/alignments">
          <div class="nav-link">Alinear</div>
        </router-link>

        <router-link to="/sequences/add">
          <div class="nav-link">Añadir nueva secuencia</div>
        </router-link>

        <router-link to="/sequences/<id>">
          <div class="nav-link">Editar secuencia</div>
        </router-link>
      </div>
  </div>
</template>

<script>
  export default {
    name: 'NavBar',
    
  }
</script>

<style scoped>
.nav-bar {
  position: relative;
  top: 0;
  min-height: 75px;
  padding: 0px 20px;
  display: flex;
  justify-content:space-between;
  align-items: center;
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
}
.nav{
  display:flex;
  flex-direction: row;
  background-color: rgba(240, 248, 255, 0.838);
  border-radius:3px;
}
.nav-link{
  margin:5px;
  padding:15px;
  font-size:100%;
  border-radius: 3px;
  
}
.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.841);
  transition: background-color 0.8s;
  box-shadow: 0px 0px 5px rgb(118, 133, 207);
}
</style>