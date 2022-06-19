<template>
    <div class="container">
        <NavBar></NavBar>
            <form>
                <label>Introduce tu secuencia: </label>
                <input type="text" name="secuencia" v-model="info.sequence" /><br>

                <label> Introduce el nombre de la especie a la que pertenece la secuencia:</label>
                <select id="category" >
                    <option v-for="category in categories" :key="category.id">
                        {{ category }}
                    </option>
                </select>

                <label>Introduce la posición de la mutación: </label>
                <input type="text" name="mut_location" v-model="info.mut_location" /> <br>

                <label>Introduce el tipo de mutación: </label>
                <input type="text" name="mutation" v-model="info.mutation" /> <br>

                <label>Introduce la información acerca de la secuencia introducida: </label>
                <input type="text" name="information" v-model="info.information" /><br>
            </form>


                <h3>Secuencia de ejemplo para hacer el alineamiento: AAAGGGCCCGGG</h3>
                <button @click.prevent="modifyEvent">Guardar</button>
                <!-- el prevent es para q se recargue la pagina cuando se da al boton de guardar -->
                
    </div>
</template>
 

<script>
import NavBar from '@/components/NavBar.vue'
export default {
    name: 'AddNewSequence',
    components:{NavBar},
    data() {
        return {
            info:{},
            categories: ["virus","bacteria","hongo","planta","animal","humano"
            ],

        };
    },
    mounted(){
        this.loadData()
    },

    methods: {
        async loadData(){
            const response = await fetch(`http://localhost:5000/api/sequences/`+ this.$route.params.id);
            this.info = await response.json();

        },
        async modifyEvent() {
            let modified_info = this.info
            const settings = {
                method: "PUT",
                body: JSON.stringify(modified_info),
                headers: {
                "Content-Type": "application/json",
                },  
                    
                };
            await fetch ('http://localhost:5000/api/sequences/' + this.$route.params.id , settings);
            },   
    },
        

}
</script>

<style>
.sequenceInfo{
    border: 1px solid black;
}
form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-bottom: 2em;
}
form label {
  font-weight: bold;
  margin-left: 50%;
}
label,
input {
  margin-top: 1em;
}
form input {
  margin-right: 40em;
  padding: 5px;
}
button {
  padding: 0 1em;
}

</style>    