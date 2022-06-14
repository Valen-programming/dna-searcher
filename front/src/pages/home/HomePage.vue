<template>
    <div id="home-page">
      <header>
    <NavBar></NavBar> 
    </header>
    <main>
      <section class="banner">
          <div class="banner-text">
            <h1>ADN SEARCHER</h1>
            <p>La mejor web de consultas de secuencias genéticas</p>
          </div>
      </section>
    </main>
    </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'Home',
  components:{NavBar},
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
#home-page{
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(180deg,#627db170 10%, #deecde8e 30%);
  }
</style>
