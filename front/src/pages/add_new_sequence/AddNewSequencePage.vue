<template>
    <div class="container">
        <NavBar></NavBar>
            <form>
                <label>Introduce tu secuencia: </label>
                <input type="text" name="secuencia" v-model="sequence" />

                <label> Introduce la categoría a la que pertenece:</label>
                <select id="category">
                    <option disable value=""></option>
                    <option v-for="category in categories" :key="category.id">
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
            </form>

                <h3>Secuencia de ejemplo para hacer el alineamiento: AAAGGGCCCGGG</h3>
                <button @click.prevent="addSequence">Guardar</button>

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
        }
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