<template>
    <div class="container">
        <NavBar></NavBar>
            <form>
                <label>Introduce tu secuencia: </label>
                <input type="text" name="secuencia" v-model="sequence" />

                <label> Introduce la categoría a la que pertenece:</label>
                <select id="category" v-model="category">
                    <option disable value=""></option>
                    <option v-for="category in categories" :value="category" :key="category.id">
                        {{ category }}
                    </option>
                </select>

                <label>Introduce el nombre de la especie a la que pertenece la secuencia: </label>
                <input type="text" name="name" v-model="name" />

                <label>Introduce la posición de la mutación: </label>
                <input type="text" name="mut_location" v-model="mut_location" />

                <label>Introduce el tipo de mutación: </label>
                <input type="text" name="mutation" v-model="mutation" />

                <label>Introduce la información acerca de la secuencia introducida: </label>
                <input type="text" name="information" v-model="information" />

                <h3>Secuencia de ejemplo para hacer el alineamiento: AAAGGGCCCGGG</h3>
                <div class="btn">
                    <button @click.prevent="addSequence">Guardar</button>
                </div>
            </form>
    </div>
</template>
 

<script>
import { v4 as uuidv4 } from "uuid";
import NavBar from '@/components/NavBar.vue'
export default {
    name: "AddNewSequence",
    components: { NavBar },
    data() {
        return {
            sequence: "",
            category: "",
            name: "",
            mutation: "",
            mut_location: "",
            information: "",
            categories: ["virus","bacteria","hongo","planta","animal","humano"
            ],
        };
    },
    mounted() {
    },
    methods: {
        async addSequence() {
            let id_sequence = uuidv4();
            let new_sequence = {
                "id": id_sequence,
                "sequence": this.sequence,
                "category":this.category,
                "name": this.name,
                "mutation": this.mutation,
                "mut_location": this.mut_location,
                "information": this.information
            };
            const settings = {
                method: "POST",
                body: JSON.stringify(new_sequence),
                headers: {
                    "Content-Type": "application/json"
                }
            };
            await fetch("http://localhost:5000/api/sequences", settings);
            console.log(new_sequence)
        }
    },
}


</script>

<style scoped>
.sequenceInfo{
    border: 1px solid black;
}
form {
  display: flex;
  flex-direction: column;  
  align-items:start;
  margin:0 auto;
  text-align: left;
  padding: 1em;
}
form label {
  font-weight: bold;

  
}
.btn{
    display:flex;
    justify-content: center;
    font-size:1.2em;
}
label,input{
    font-size:1.2em;
}
button {
  font-size: 1em;
  border-radius: 7px;
  border: black solid 1.5px;
  background-color: rgba(224, 224, 239, 0.77);
  cursor: pointer;

}

@media(min-width:1000px){
form {
 max-width: 900px;
 display: grid;
 grid-template-columns: 1fr 1fr;
}

}
form label + input, select{
    margin-bottom: 1em;
}

</style>