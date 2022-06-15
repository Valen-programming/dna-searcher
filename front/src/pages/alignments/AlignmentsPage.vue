<template>
    <div class="container">
        <NavBar></NavBar>
        <label>Introduce tu secuencia: </label>
        <input type="text" name="secuencia" v-model="sequence" />
        <h3>Secuencia de ejemplo para hacer el alineamiento: AAAGGGCCCGGG</h3>
        <button @click.prevent="alignSequence">Alinear</button>

        <div class="sequenceInfo">
            <h2 class="sequence" @click="this.$router.push({name: 'EditSequence', params:{id:sequence_info_from_db.id}})">{{sequence_info_from_db.sequence}}</h2>
            <h2 class="name">{{sequence_info_from_db.name}}</h2>
            <h2 class="mut_location">{{sequence_info_from_db.mut_location}}</h2>
            <h2 class="information">{{sequence_info_from_db.information}} </h2>
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

<style>
.sequenceInfo{
    border: 1px solid black;
    justify-content: stretch;
}

</style>