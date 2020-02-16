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
                            <input id="name" v-model="name" placeholder="name" autocomplete="off" required="" aria-required="true">
                        </p>
                        <p>
                            <label for="photographer">Photographer:</label>
                            <input id="photographer" v-model="photographer" placeholder="photographer">
                        </p>
                        <p>
                            <label for="name">Model:</label>
                            <input id="model" v-model="model" placeholder="model">
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
                        <i class="material-icons left">error</i>{{ errorMsg }}
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
                photographer: null,
                model: null,
                submited: false,
                success: false,
                errorMsg: 'Something went wrong, please try again =S',
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
                this.photographer = null;
                this.model = null;
                this.submited = false;
                this.success = false;
                this.errorMsg = 'Something went wrong, please try again =S';
            },
            onSubmit() {
                axios.post(`${process.env.VUE_APP_API_URL}/gallery`, {
                    gallery_name: this.name,
                    photographer: this.photographer,
                    model: this.model 
                }).then(response => {
                    this.submited = true;
                    this.success = true;
                    this.$emit('gallery-added', response.data.gallery);
                }).catch(error => {
                    this.submited = true;
                    this.success = false;
                    this.errorMsg = error.response.data;
                });
            }
        }
    }
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>