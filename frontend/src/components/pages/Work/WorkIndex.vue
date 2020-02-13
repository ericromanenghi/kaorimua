<template>
    <div>
        <HorizontalPage v-if='!displayError'>
            <WorkThumbnail isMenuItem='1' />
            <WorkThumbnail v-for='work in works' v-bind:key='work.slug' :work=work />
        </HorizontalPage>
        <PageError v-if='displayError' />
    </div>
</template>

<script>
import WorkThumbnail from './../../partials/WorkThumbnail'
import HorizontalPage from './../../partials/HorizontalPage'
import PageError from './../../partials/PageError'
import { EventBus } from '../../eventBus'

export default {
    data: function () {
        return {
            endpoint: `${process.env.VUE_APP_API_URL}gallery/all`,
            works: [],
            displayError: false,
        }
    },
    components: {
        WorkThumbnail,
        HorizontalPage,
        PageError,
    },
    methods: {
        renderPhotos (response) {
            EventBus.$emit('loading:end')
            this.works = response.data.galleries.map(work => {
                return {
                    ...work,
                    src: `${process.env.VUE_APP_API_IMAGE_BASE}${work.photos[0].filename}`
                }
            })
            setTimeout(() => {
                EventBus.$emit('workPhoto:resized')
            }, 10)
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

<style lang='scss' src="@/scss/work/list.scss"></style>
