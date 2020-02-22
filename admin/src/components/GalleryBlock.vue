<template>
    <div>
        <h4 @click="toggleActive">{{ name }}</h4>
        <div v-if="active"> 
            <p>
                <photo-upload :gallery_id="id"></photo-upload>
            </p>
            <p>
                <gallery-edit :gallery_id="id" :name="name" :photographer="photographer" :model="model"></gallery-edit>
            </p>
            <p>
                Photographer: {{ photographer }}
            </p>
            <p>
                Model: {{ model }}
            </p>
            <gallery-photos :gallery_id="id"></gallery-photos>
        </div>
    </div>
</template>

<script>
import PhotoUpload from './PhotoUpload.vue';
import GalleryEdit from './GalleryEdit.vue';
import GalleryPhotos from './GalleryPhotos.vue';

export default {
    components: {
        PhotoUpload,
        GalleryEdit,
        GalleryPhotos
    },
    props: ['id', 'name', 'photographer', 'model'],
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