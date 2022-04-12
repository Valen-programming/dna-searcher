<template>
    <label>Introduce tu secuencia: </label>
    <input type="text" name="secuencia" v-model="sequence" />
    <button @click.prevent="alignSequence">Alinear</button>
</template>

<script>
export default {
    name: 'Alignments',
    data() {
        return {
            sequence: "",
            // dataBaseSequence: {}
        }
    },
    mounted(){
        // this.loadData()
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
            this.dataBaseSequence = await response.json()
            console.log(this.sequence)
        }  
        
    }
}


</script>

<style>

</style>