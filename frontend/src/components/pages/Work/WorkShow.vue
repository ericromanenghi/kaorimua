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
            work: {
                title: 'Karolijn',
                src: `${process.env.BASE_URL}photos/works/karolijn.jpg`,
                makeup: 'Kaori',
                model: 'Karolijn',
                photographer: 'Celia',
            },
            photos: [{
                ratio: 66.6666,
                src: `${process.env.BASE_URL}photos/works/karolijn.jpg`,
            }, {
                ratio: 125,
                src: `${process.env.BASE_URL}photos/works/aleksandra.jpg`,
            }, {
                ratio: 125,
                src: `${process.env.BASE_URL}photos/works/monica.jpg`,
            }, {
                ratio: 75,
                src: `${process.env.BASE_URL}photos/works/magda.jpg`,
            }],
        }
    },
    components: {
        WorkThumbnail,
        WorkPhoto,
        WorkDescription,
        HorizontalPage,
    },
}
</script>

<style lang='scss' src='@/scss/work/list.scss' scoped></style>
