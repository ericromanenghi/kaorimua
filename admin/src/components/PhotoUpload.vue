<template>
    <div id="photo-upload-container">
        <a @click="onCreate()" class="waves-effect waves-light btn modal-trigger" :href="'#modal-photo-upload'+gallery_id">
            Upload photo
        </a>
        <div :id="'modal-photo-upload'+gallery_id" class="modal">
            <div class="modal-content">
                <div v-if="!submited" class="upload-photo-form">
                    <h3>Upload photo</h3>
                    <form class="" @submit.prevent="onSubmit">
                        <p>
                            <label for="name">Photo name:</label>
                            <input :id="'photo-name-'+gallery_id" v-model="photo_name" placeholder="name">
                        </p>
                        <p>
                            <button class="btn waves-effect waves-light" type="submit" name="action">
                                Submit
                                <i class="material-icons right">send</i>
                            </button>
                        </p>
                    </form>
                </div>
                <div v-else class="photo-upload-msg">
                    <p v-if="success" class="green-text">
                        <i class="material-icons left">check</i>Photo successfully added to gallery!
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
    props: ['gallery_id'],
    data() {
        return {
            photo_name: null,
            display_form: false,
            submited: false,
            success: false,
        };
    },
    mounted() {
        let elems = this.$el.querySelectorAll('.modal');
        // eslint-disable-next-line
        let instances = M.Modal.init(elems);
    },
    methods: {
        onCreate() {
            this.photo_name = null;
            this.submited = false;
            this.success = false;
            this.display_form = true;
        },
        onSubmit() {
            axios.post("http://localhost:5000/photo", {
                file_name: this.photo_name,
                gallery_id: this.gallery_id
            }).then(response => {
                this.submited = true;
                this.success = true;
                this.$emit('photo-added', response.data);
            }).catch(error => {
                this.submited = true;
                this.success = false;
                console.log(error);
            });
        }
    }
}
</script>
