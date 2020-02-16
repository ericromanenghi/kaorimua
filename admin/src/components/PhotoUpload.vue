<template>
    <div id="photo-upload-container">
        <a @click="displayUploadPhoto()" class="waves-effect waves-light btn modal-trigger" :href="'#'+modal_id">
            Upload photo
        </a>
        <div :id="modal_id" class="modal">
            <div class="modal-content">
                <div v-if="!submited" class="upload-photo-form">
                    <h3>Upload photo</h3>
                    <p>
                        <label>Photo name:
                            <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
                        </label>
                    </p>
                    <p>
                        <button v-on:click="submitFile()" class="btn waves-effect waves-light">
                            Submit
                            <i class="material-icons right">send</i>
                        </button>
                    </p>
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
            submited: false,
            success: false,
            modal_id: '',
            file: ''
        };
    },
    mounted() {
        this.modal_id = 'modal-photo-upload' + this.gallery_id;
        let elems = this.$el.querySelectorAll('.modal');
        // eslint-disable-next-line
        let instances = M.Modal.init(elems);
    },
    methods: {
        displayUploadPhoto() {
            this.photo_name = null;
            this.submited = false;
            this.success = false;
        },
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
        },
        submitFile() {
            let formData = new FormData();
            formData.append('file', this.file);
            formData.append('gallery_id', this.gallery_id)
            axios.post(`${process.env.VUE_APP_API_URL}/photo`,
                formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
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
