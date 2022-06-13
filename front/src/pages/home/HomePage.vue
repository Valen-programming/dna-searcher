<template>
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

header {
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
h1{
  font-size:8vw;
  color:blue;
}
p{
  font-size:2.5vw;
}
.banner{
  width:68%;
  height: 50%;
  margin:0px auto;
  padding:8vw;
  background-color: rgba(240, 248, 255, 0.55);
  display:flex;
  align-items: center;
  justify-content: center;
  
}

</style>
