<template>
  <div class="nav-bar">
     <div class="logo">
          <img id="header-img" src="@/assets/img/logo.png" alt="adn searcher logo" />
      </div>
      <div class="nav">
        <div class="nav-link">
          <router-link to="/">Home </router-link>
        </div>
        <div class="nav-link">
          <router-link to="/about">About </router-link>  
        </div>
        <div class="nav-link">
          <router-link to="/alignments">Alinear</router-link>
        </div>
        <div class="nav-link">
          <router-link to="/sequences/add">Añadir nueva secuencia</router-link>
        </div>
        <div class="nav-link">
          <router-link to="/sequences/<id>">Editar secuencia</router-link>
        </div>
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
}
.nav{
  display:flex;
  flex-direction: row;
  background-color: rgba(240, 248, 255, 0.285);
}
.nav-link{
  margin:10px;
  padding:15px;
  font-size:100%;
  border-radius: 3px;
}
.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.747);
  transition: background-color 0.8s;
}
</style>