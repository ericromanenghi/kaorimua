<template>
    <div class="container">
        <div class="row valign-wrapper">
            <div class="col s6">
                <h1>Galleries</h1>
            </div>
            <div class="col s6">
                <create-gallery v-on:gallery-added="refreshGalleries"></create-gallery>
            </div>
        </div>
        <div id="galleries-list">
            <div v-for="gallery in galleries" v-bind:key="gallery.id"> 
                <gallery-block :id="gallery.id" :name="gallery.name" :photographer="gallery.photographer" :model="gallery.model"></gallery-block>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

import CreateGallery from './CreateGallery.vue';
import GalleryBlock from './GalleryBlock.vue';

export default {
    components: {
        CreateGallery,
        GalleryBlock
    },
    data() {
        return {
            galleries: []
        }
    },
    mounted() {
        axios.get(`${process.env.VUE_APP_API_URL}/gallery/all?allow_empty=1`).then(response => {
            this.galleries = response.data.galleries;
        });
    },
    methods: {
        refreshGalleries(gallery) {
            this.galleries.push(gallery);
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>