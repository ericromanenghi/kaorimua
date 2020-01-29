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
            works: [{
                slug: 'karolijn',
                title: 'Karolijn',
                photo: `${process.env.BASE_URL}photos/works/karolijn.jpg`,
            }, {
                slug: 'aleksandra',
                title: 'Aleksandra',
                photo: `${process.env.BASE_URL}photos/works/aleksandra.jpg`,
            }, {
                slug: 'monica',
                title: 'Monica',
                photo: `${process.env.BASE_URL}photos/works/monica.jpg`,
            }, {
                slug: 'magda',
                title: 'Magda',
                photo: `${process.env.BASE_URL}photos/works/magda.jpg`,
            }]
        }
    },
    components: {
        WorkThumbnail,
        HorizontalPage,
    },
}
</script>

<style lang='scss' src="@/scss/work/list.scss" scoped></style>
