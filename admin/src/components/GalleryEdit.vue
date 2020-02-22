<template>
    <div id="gallery-edit-container">
        <a @click="displayGalleryEdit()" class="waves-effect waves-light btn modal-trigger" :href="'#'+modal_id">
            Edit gallery
        </a>
        <div :id="modal_id" class="modal">
            <div class="modal-content">
                <div v-if="!submited" class="upload-photo-form">
                    <h3>Edit gallery</h3>
                    <p>
                        <label for="name">Gallery name:</label>
                        <input :id="modal_id + '-name'" v-model="new_name" placeholder="name" autocomplete="off" required="" aria-required="true">
                    </p>
                    <p>
                        <label for="photographer">Photographer:</label>
                        <input :id="modal_id + '-photographer'" v-model="new_photographer" placeholder="photographer">
                    </p>
                    <p>
                        <label for="name">Model:</label>
                        <input :id="modal_id + '-model'" v-model="new_model" placeholder="model">
                    </p>
                    <p>
                        <button v-on:click="onSubmit()" class="btn waves-effect waves-light">
                            Submit
                            <i class="material-icons right">send</i>
                        </button>  
                    </p>
                </div>
                <div v-else class="gallery-edit-msg">
                    <p v-if="success" class="green-text">
                        <i class="material-icons left">check</i>Gallery successfully edited!
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
    props: ['gallery_id', 'name', 'photographer', 'model'],
    data() {
        return {
            submited: false,
            success: false,
            modal_id: '',
            new_name: '',
            new_photographer: '',
            new_model: '',
        };
    },
    mounted() {
        this.modal_id = 'modal-gallery-edit' + this.gallery_id;
        let elems = this.$el.querySelectorAll('.modal');
        // eslint-disable-next-line
        let instances = M.Modal.init(elems);
        this.new_name = this.name;
        this.new_photographer = this.photographer;
        this.new_model = this.model;
    },
    methods: {
        displayGalleryEdit() {
            this.submited = false;
            this.success = false;
        },
        onSubmit() {
            axios.post(`${process.env.VUE_APP_API_URL}/gallery/${this.gallery_id}`, {
                gallery_name: this.new_name,
                photographer: this.new_photographer,
                model: this.new_model 
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
