<template>
    <div class="container">
        <NavBar></NavBar>
            <form>
                <label>Introduce tu secuencia: </label>
                <input type="text" name="secuencia" v-model="info.sequence" />

                <label> Introduce la categoría a la que pertenece: </label>
                <select id="category" v-model="info.category" >
                    <option v-for="category in categories" :key="category.id">
                        {{ category }}
                    </option>
                </select>

                <label>Introduce el nombre de la especie a la que pertenece la secuencia: </label>
                <input type="text" name="name" v-model="info.name" />

                <label>Introduce la posición de la mutación: </label>
                <input type="text" name="mut_location" v-model="info.mut_location" /> 

                <label>Introduce el tipo de mutación: </label>
                <input type="text" name="mutation" v-model="info.mutation" /> 

                <label>Introduce la información acerca de la secuencia introducida: </label>
                <input type="text" name="information" v-model="info.information" />
               
                <div class="btn">
                    <button @click="modifyEvent">Guardar</button>
                </div>
            </form>


                
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
        isValidSequenceModified() {
          if (
            this.info.sequence === "" ||
            this.info.category === "" ||
            this.info.name === "" ||
            this.info.mutation === "" ||
            this.info.mut_location === "" ||
            this.info.information === ""
          ) {
            return false;
          } else {
            return true;
          }
        },
        async modifyEvent() {
            if (!this.isValidSequenceModified()) {
                alert("Se deben rellaner todos los campos");
                return;
            }
            let modified_info = this.info
            const settings = {
                method: "PUT",
                body: JSON.stringify(modified_info),
                headers: {
                "Content-Type": "application/json",
                },  
                    
                };
            await fetch ('http://localhost:5000/api/sequences/' + this.$route.params.id , settings);
            alert("Evento guardado correctamente");
            this.$router.push("/");
            },   
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
    font-size: 1.2em;
}
label, input{
  font-size: 1.2em;
}
button {
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