<template>
    <div class="row">
        <div v-for="photo in photos" v-bind:key="photo.id" class="photo-container col s6">
                <img :src="`${base_img_path}/${photo.filename}`" class="responsive-img gallery-photo">
                <a v-on:click="deletePhoto(photo)" class="btn-floating btn-small waves-effect waves-light red">
                    <i class="material-icons">delete</i>
                </a>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    props: ['gallery_id'],
    data() {
        return {
            photos: [],
            base_img_path: `${process.env.VUE_APP_API_IMAGE_BASE}`,
        };
    },
    mounted() {
        this.getImages();
    },
    methods: {
        getImages() {
            let formData = new FormData();
            formData.append('file', this.file);
            formData.append('gallery_id', this.gallery_id)
            axios.get(
                `${process.env.VUE_APP_API_URL}/gallery/${this.gallery_id}/photos`
            ).then(response => {
                this.photos = response.data.photos;
            });
        },
        deletePhoto: function(photo) {
            axios.delete(
                `${process.env.VUE_APP_API_URL}/photo/${photo.id}`,
            ).then(function() {
                this.photos.splice(this.photos.indexOf(photo), 1)
            });
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.gallery-photo {
    max-height: 300px;
    padding: 10px;
}

.photo-container {
    position: relative;
}

.photo-container a {
    position: absolute;
    top: 8%;
    left: 10%;
}

</style>
