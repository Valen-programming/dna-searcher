<template>
  <body>
    <header>
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
     
    </header>
    <main>
      <section class="banner">
          <div class="banner-text">
            <h1>ADN SEARCHER</h1>
            <p>La mejor web de consultas de secuencias genéticas</p>
          </div>
      </section>
    </main>
  </body>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      info: {}
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/info')
      this.info = await response.json()
    }
  }


}
</script>

<style scoped>
*{
  margin:0;
  padding:0;
  box-sizing: border-box;
}
body{
  background:linear-gradient(rgba(0, 0, 0, 0.356),#009688),url(banner.jpg);
  background-size: cover;
  background-position: center;
  height:100vh;
  width:100vw;
  
}
header {
  position: relative;
  top: 0;
  min-height: 75px;
  padding: 0px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo > img {
  max-width: 80px;
  margin-left: 10px;
  margin-top: 10px;
  width:60%;
}
.nav{
  display:flex;
  flex-direction: row;
  justify-content: space-around;
}
.nav-link{
  margin:10px;
  margin-right: 10px;
}
h1{
  font-size:9vw;
  color:whitesmoke;
}
.banner{
  width:68%;
  height: 50%;
  margin:auto;
  padding:8vw;
  background-color: rgba(240, 248, 255, 0.244);
  
}

</style>
