<template>
    <div>
        <div class="row">
            <div class="col s12">
                <h4 @click="toggleActive">{{ name }}</h4>
            </div>
        </div>
        <div v-if="active">
            <div class="row">
                <div class="col s3">
                    <photo-upload :gallery_id="id"></photo-upload>
                </div>
                <div class="col s3">
                    <gallery-edit :gallery_id="id" :name="name" :photographer="photographer" :model="model"></gallery-edit>
                </div>
            </div>
            <div class="row">
                <div class="col s12">
                    Photographer: {{ photographer }}
                </div>
            </div>
            <div class="row">
                <div class="col s12">
                    Model: {{ model }}
                </div>
            </div>
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