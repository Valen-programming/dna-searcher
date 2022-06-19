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
        <article class="event" v-for="event in sequenceInfo" :key="event.id">
            <div class="text-article">
              <h2>{{ event.sequence }}</h2>
              <p>{{ event.name }}</p>
              <p>{{ event.mutation }}</p>
              <p>{{ event.mut_location }}</p>
              <p>{{ event.information }}</p>
              <button @click="editSequence(event)"></button>
            </div>
        </article>

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
    mounted() {
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

<style scope>

.categories-container{
  border:solid black 2px;
  padding: 10px;
  background-color: rgba(240, 255, 255, 0.801);
  margin: 1rem 5rem;
}
#category-img{
  max-width: 100px;
  margin: 7px;
  width:100%;
  border-radius: 10px;
}
.link-category{
  margin: 0px 8px 0px 0px;
  padding:0px 16px 0px 0px;
 
}
.link-category:hover {
  background-color: rgba(255, 255, 255, 0.841);
  transition: background-color 0.8s;
  box-shadow: 0px 0px 5px rgb(118, 133, 207);
  border-radius: 10px;
}
.text-article{
  border:solid blueviolet 2px;
  margin-bottom:10px;
  background-color: rgba(255, 255, 255, 0.841);
}

</style>