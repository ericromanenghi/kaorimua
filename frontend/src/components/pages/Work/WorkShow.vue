<template>
    <div>
        <div class='work' v-if='!displayError'>
            <HorizontalPage class='work__list'>
                <WorkThumbnail isMenuItem='1' />
                <WorkDescription :work='work'/>
                <WorkPhoto v-for='photo in photos' v-bind:key='photo.src' :photo=photo />
            </HorizontalPage>
        </div>
        <PageError v-if='displayError' />
    </div>
</template>

<script>
import WorkThumbnail from './../../partials/WorkThumbnail'
import HorizontalPage from './../../partials/HorizontalPage'
import WorkPhoto from './../../partials/WorkPhoto'
import WorkDescription from './../../partials/WorkDescription'
import PageError from './../../partials/PageError'
import { EventBus } from '../../eventBus'

export default {
    data () {
        return {
            endpoint: `${process.env.VUE_APP_API_URL}gallery/${this.$route.params.id}`,
            work: {},
            photos: [],
            displayError: false,
        }
    },
    components: {
        WorkThumbnail,
        WorkPhoto,
        WorkDescription,
        HorizontalPage,
        PageError,
    },
    methods: {
        renderPhotos (response) {
            EventBus.$emit('loading:end')
            const data = response.data.gallery
            this.photos = data.photos.map(photo => {
                return {
                    src: `${process.env.VUE_APP_API_IMAGE_BASE}${photo.filename}`,
                    ratio: photo.width / photo.height * 100,
                }
            })
            this.work = {
                ...data,
                src: `${this.photos[0].src}`,
            }
        },
        handleError () {
            EventBus.$emit('loading:end')
            this.displayError = true
        },
    },
    mounted () {
        EventBus.$emit('loading:start')
        this.$http.get(this.endpoint).then(this.renderPhotos).catch(this.handleError)
    }
}
</script>

<style lang='scss' src='@/scss/work/list.scss' scoped></style>
