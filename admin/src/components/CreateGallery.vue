<template>
    <div id="create-gallery-container">
        <a @click="onCreate" class="btn-floating btn-large waves-effect waves-light red modal-trigger" href="#modal1">
            <i class="material-icons">add</i>
        </a>
        <div id="modal1" class="modal">
            <div class="modal-content">
                <div v-if="!submited" id="create-form">
                    <h3>Create gallery</h3>
                    <form class="add-gallery" @submit.prevent="onSubmit">
                        <p>
                            <label for="name">Gallery name:</label>
                            <input id="name" v-model="name" placeholder="name">
                        </p>
                        <p>
                            <button class="btn waves-effect waves-light" type="submit" name="action">
                                Submit
                                <i class="material-icons right">send</i>
                            </button>  
                        </p>
                    </form>
                </div>
                <div v-else id="sucess-msg">
                    <p v-if="success" class="green-text">
                        <i class="material-icons left">check</i>Gallery created!
                    </p>
                    <p v-else class="red-text">
                        <i class="material-icons left">error</i>Something went wrong, please try again =S
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                name: null,
                submited: false,
                success: false,
            }
        },
        mounted() {
            let elems = this.$el.querySelectorAll('.modal');
            // eslint-disable-next-line
            let instances = M.Modal.init(elems);
        },
        methods: {
            onCreate() {
                this.name = null;
                this.submited = false;
                this.success = false;
            },
            onSubmit() {
                axios.post("http://localhost:5000/gallery", {
                    gallery_name: this.name 
                }).then(response => {
                    this.submited = true;
                    this.success = true;
                    this.$emit('gallery-added', response.data.gallery);
                }).catch(error => {
                    this.submited = true;
                    this.success = false;
                    console.log(error);
                });
            }
        }
    }
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>