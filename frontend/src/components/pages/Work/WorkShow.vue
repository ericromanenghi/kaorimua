<template>
    <div>
        <div class='work'>
            <HorizontalPage class='work__list'>
                <WorkThumbnail isMenuItem='1' />
                <WorkDescription :work='work'/>
                <WorkPhoto v-for='photo in photos' v-bind:key='photo.src' :photo=photo />
            </HorizontalPage>
        </div>
    </div>
</template>

<script>
import WorkThumbnail from './../../partials/WorkThumbnail'
import HorizontalPage from './../../partials/HorizontalPage'
import WorkPhoto from './../../partials/WorkPhoto'
import WorkDescription from './../../partials/WorkDescription'

export default {
    data () {
        return {
            endpoint: `${process.env.VUE_APP_API_URL}gallery/${this.$route.params.id}`,
            work: {},
            photos: [],
        }
    },
    components: {
        WorkThumbnail,
        WorkPhoto,
        WorkDescription,
        HorizontalPage,
    },
    methods: {
        renderPhotos (response) {
            const data = response.data.gallery
            this.photos = data.photos.map(photo => {
                return {
                    src: `${process.env.VUE_APP_API_IMAGE_BASE}${photo.filename}`,
                    ratio: 66.6666
                }
            })
            this.work = {
                name: data.name,
                src: `${this.photos[0].src}`,
            }
        }
    },
    mounted () {
        this.$http.get(this.endpoint).then(this.renderPhotos)
    }
}
</script>

<style lang='scss' src='@/scss/work/list.scss' scoped></style>
