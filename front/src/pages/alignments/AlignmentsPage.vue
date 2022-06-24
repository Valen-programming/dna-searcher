<template>
    <div class="container">
        <NavBar></NavBar>

        <div class="container-info">
            <div class="text">
                <label>Introduce tu secuencia: </label>
                <input type="text" name="secuencia" v-model="sequence" />
            </div>
            <h3>Secuencia de ejemplo para hacer el alineamiento: AAAGGGCCCGGG</h3>
            <div class="btn">
                <button @click.prevent="alignSequence">Alinear</button>
            </div>
        </div>
        <div class="article-container">
            <div class="article">
                <h2 class="sequence" @click="this.$router.push({name: 'EditSequence', params:{id:sequence_info_from_db.id}})">{{sequence_info_from_db.sequence}}</h2>
                <h2 class="category">{{sequence_info_from_db.category}}</h2>
                <h2 class="name">{{sequence_info_from_db.name}}</h2>
                <h2 class="mut_location">{{sequence_info_from_db.mut_location}}</h2>
                <h2 class="information">{{sequence_info_from_db.information}} </h2>
            </div>
        </div>
    </div>
</template>
 

<script>
import NavBar from '@/components/NavBar.vue'
export default {
    name: 'Alignments',
    components:{NavBar},
    data() {
        return {
            sequence: "",
            sequence_info_from_db: {}
            
        }
    },
    mounted(){
        
    },
    methods: {
        
        async alignSequence(){
            let new_sequence = {'sequence': this.sequence}
            const settings = {
                method: 'POST',
                body: JSON.stringify(new_sequence),
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            const response = await fetch ('http://localhost:5000/api/alignments', settings)
            this.sequence_info_from_db= await response.json()
            
        }  
        
    }
}


</script>

<style scoped>
.container-info{
    display:grid;
    grid-template-columns: 1fr;
    margin: 10px auto;
    position:relative;
    padding:50px;
    background-color: rgba(240, 255, 255, 0.801);
}
.article-container{
  display:grid;
  grid-template-columns: 1fr;
  margin: 10px auto;
  position:relative;
  padding:15px;
  border:solid blueviolet 2px;
  background-color: rgba(255, 255, 255, 0.941);
  border-radius: 5px;
}
button{
    font-size:1.2em;
    cursor: pointer;

}

</style>