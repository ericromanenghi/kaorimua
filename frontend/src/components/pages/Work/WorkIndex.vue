<template>
    <div>
        <div class='work'>
            <HorizontalPage class='work__list'>
                <WorkThumbnail isMenuItem='1' />
                <WorkThumbnail v-for='work in works' v-bind:key='work.slug' :work=work />
            </HorizontalPage>
        </div>
    </div>
</template>

<script>
import WorkThumbnail from './../../partials/WorkThumbnail'
import HorizontalPage from './../../partials/HorizontalPage'

export default {
    data: function () {
        return {
            endpoint: `${process.env.VUE_APP_API_URL}gallery/all`,
            works: []
        }
    },
    components: {
        WorkThumbnail,
        HorizontalPage,
    },
    methods: {
        renderPhotos (response) {
            this.works = response.data.galleries.map(work => {
                return {
                    ...work,
                    src: `${process.env.VUE_APP_API_IMAGE_BASE}${work.photos[0].filename}`
                }
            })
        }
    },
    mounted () {
        this.$http.get(this.endpoint).then(this.renderPhotos)
    }
}
</script>

<style lang='scss' src="@/scss/work/list.scss" scoped></style>
