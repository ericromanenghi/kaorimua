<template>
    <div>
        <h4 @click="toggleActive">{{ name }}</h4>
        <p v-if="active">
            <photo-upload :gallery_id="id"></photo-upload>
        </p>
        <gallery-photos :gallery_id="id"></gallery-photos>
    </div>
</template>

<script>
import PhotoUpload from './PhotoUpload.vue';
import GalleryPhotos from './GalleryPhotos.vue';

export default {
    components: {
        PhotoUpload,
        GalleryPhotos
    },
    props: ['name', 'id'],
    data() {
        return {
            active: false
        };
    },
    mounted() {
        this.active = false;
    },
    methods: {
        toggleActive() {
            this.active = !this.active;
        }
    }
}
    
</script>