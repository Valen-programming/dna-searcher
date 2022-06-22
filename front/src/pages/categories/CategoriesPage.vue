<template>
    <div class="container">
        <NavBar></NavBar>

        <div class="categories-container">
            <button class="link-category" @click="getVirusSequences">
              <img id="category-img" src="@/assets/img/virus.jpeg" alt="adn searcher logo" />
              <span>Virus</span>
            </button>
            <button class="link-category" @click="getBacteriaSequences">
              <img id="category-img" src="@/assets/img/bacteria.jpg" alt="adn searcher logo" />
              <span>Bacteria</span>
            </button>
            <button class="link-category" @click="getFungiSequences">
              <img id="category-img" src="@/assets/img/hongo.jpg" alt="adn searcher logo" />
              <span>Hongo</span>
            </button>
            <button class="link-category" @click="getPlantSequences">
              <img id="category-img" src="@/assets/img/planta.png" alt="adn searcher logo" />
              <span>Planta</span>
            </button>
            <button class="link-category" @click="getAnimalSequences">
              <img id="category-img" src="@/assets/img/animal.jpg" alt="adn searcher logo" />
              <span>Animal</span>
            </button>
            <button class="link-category" @click="getHumanSequences">
              <img id="category-img" src="@/assets/img/humano.jpeg" alt="adn searcher logo" />
              <span>Humano</span>
            </button>
        </div>
        <div class="article-container">
          <article class="event" v-for="event in sequenceInfo" :key="event.id">
              <div class="text-article">
                <h2>{{ event.sequence }}</h2>
                <p>{{ event.name }}</p>
                <p>{{ event.mutation }}</p>
                <p>{{ event.mut_location }}</p>
                <p>{{ event.information }}</p>
                <div class="btn">
                  <button @click="editSequence(event)">Editar</button>
                </div>
              </div>
          </article>
        </div>
    </div>
</template>
 

<script>
import NavBar from '@/components/NavBar.vue'
export default {
    name: "Categories",
    components: { NavBar },
    data() {
        return {
            sequenceInfo:[],
        };
    },
    methods: {
        async getVirusSequences(){
            const response =await fetch('http://localhost:5000/api/categories/virus');
            this.sequenceInfo = await response.json();
        },
        async getBacteriaSequences(){
            const response =await fetch('http://localhost:5000/api/categories/bacteria');
            this.sequenceInfo = await response.json();
        },
        async getFungiSequences(){
            const response =await fetch('http://localhost:5000/api/categories/hongo');
            this.sequenceInfo = await response.json();
        },
        async getPlantSequences(){
            const response =await fetch('http://localhost:5000/api/categories/planta');
            this.sequenceInfo = await response.json();
        },
        async getAnimalSequences(){
            const response =await fetch('http://localhost:5000/api/categories/animal');
            this.sequenceInfo = await response.json();
        },
        async getHumanSequences(){
            const response =await fetch('http://localhost:5000/api/categories/humano');
            this.sequenceInfo = await response.json();
        },
        editSequence(event){
          this.$router.push("/sequences/" + event.id)
        }
    },
}


</script>

<style scoped>

.categories-container{
  display:grid;
  grid-template-columns: 1fr 1fr 1fr;
  border:solid black 2px;
  padding: 10px 25px;
  background-color: rgba(240, 255, 255, 0.801);
  margin:auto;
  position: relative;
  justify-content: space-between;
}
.link-category{
  width: 200px;
  padding: 3px 3px 4px;
  border-radius: 8px;
  margin:20px;
  background-color: rgb(142, 200, 218);
  display: inline-block;  
  justify-content: center;
}
.link-category:hover {
  background-color: rgba(255, 255, 255, 0.841);
  transition: background-color 0.8s;
  box-shadow: 0px 0px 5px rgb(118, 133, 207);
  border-radius: 10px;
  cursor: pointer;

}
#category-img{
  max-width: 180px;
  margin: 7px;
  width:100%;
  border-radius: 10px;
}
.article-container{
  display:grid;
  grid-template-columns: 1fr;
  margin: 10px auto;
  position:relative;
  padding:3px;
  
}
.text-article{
  border:solid blueviolet 2px;
  background-color: rgba(255, 255, 255, 0.941);
  margin:10px auto;
  padding:5px;
  border-radius: 5px;
  overflow: hidden;
}
button {
  font-size: 1em;
  border-radius: 7px;
  border: black solid 1.5px;
  background-color: rgba(224, 224, 239, 0.77);
  cursor: pointer;

}
@media(max-width: 750px){
  .categories-container{
    grid-template-columns: 1fr 1fr;
  
  }
}
@media(max-width: 500px){
  .categories-container{
    grid-template-columns: 1fr;
  
  }
}

</style>