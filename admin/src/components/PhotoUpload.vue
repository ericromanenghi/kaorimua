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
                            <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" multiple/>
                        </label>
                    </p>
                    <p>
                        Size: {{ size.toFixed(2) }} MB
                    <p>
                        <button v-on:click="submitFile()" class="btn waves-effect waves-light">
                            Submit
                            <i class="material-icons right">send</i>
                        </button>
                    </p>
                    <p v-if="size > 250" class="red-text">
                        Maximum allowed size of upload is 250 MB
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
            submited: false,
            success: false,
            modal_id: '',
            files: '',
            size: 0
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
            this.submited = false;
            this.success = false;
        },
        handleFileUpload() {
            this.files = this.$refs.file.files;
            this.size = Array.from(this.files).map(e => e.size).reduce((acc, cur) => acc + cur) / 1000000.0;
        },
        submitFile() {
            let formData = new FormData();
            Array.from(this.files).forEach(e => formData.append('file', e));
            formData.append('gallery_id', this.gallery_id)
            axios.post(`${process.env.VUE_APP_API_URL}/photo`,
                formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {
                this.$emit('photo-added', response.data);
                this.resetValues(true, true);
            }).catch(function() {
                this.resetValues(true, false);
            });
        },
        resetValues(submited, success) {
            this.submited = submited;
            this.success = success;
            this.modal_id = '';
            this.files = '';
            this.size = 0;
        }
    }
}
</script>
