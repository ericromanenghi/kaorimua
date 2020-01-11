<template>
    <div>
        <div class='work'>
            <div class='work__list' ref='list'>
                <WorkThumbnail isMenuItem='1' />
                <WorkThumbnail v-for='work in works' v-bind:key='work.slug' :work=work />
            </div>
        </div>
    </div>
</template>

<script>
import WorkThumbnail from './../../partials/WorkThumbnail'

export default {
    data: function () {
        return {
            works: [{
                slug: 'karolijn',
                title: 'Karolijn',
                photo: `${process.env.BASE_URL}photos/karolijn.jpg`,
            }, {
                slug: 'aleksandra',
                title: 'Aleksandra',
                photo: `${process.env.BASE_URL}photos/aleksandra.jpg`,
            }, {
                slug: 'monica',
                title: 'Monica',
                photo: `${process.env.BASE_URL}photos/monica.jpg`,
            }, {
                slug: 'magda',
                title: 'Magda',
                photo: `${process.env.BASE_URL}photos/magda.jpg`,
            }]
        }
    },
    components: {
        WorkThumbnail,
    },
    methods: {
        resizeBody () {
            if (window.innerWidth > 700) {
                document.body.style.height = this.$refs.list.scrollWidth + 'px'
                window.addEventListener('scroll', this.handleScroll)
            } else {
                document.body.style.height = 'auto'
                window.removeEventListener('scroll', this.handleScroll)
            }
        },
        handleScroll () {
            const percentageScrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight)
            this.$refs.list.style.transform = 'translateX(-' + (percentageScrolled * (this.$refs.list.scrollWidth - window.innerWidth)) + 'px)'
        }
    },
    mounted () {
        this.resizeBody()
        window.addEventListener('resize', this.resizeBody)
    },
    destroyed () {
        document.body.style.height = 'auto'
        window.removeEventListener('resize', this.resizeBody)
        window.removeEventListener('scroll', this.handleScroll)
    }
}
</script>

<style lang='scss' scoped>
@import './../../../scss/variables.scss';

.work {
    height: calc(100vh - 164px);
    margin: 10px;
    overflow-x: auto;
}
.work__list {
    display: flex;
    flex-wrap: nowrap;
}

@media screen and (min-width: 700px) {
    .work {
        height: 100%;
        left: 0;
        overflow: hidden;
        margin: 15px 15px 15px 0;
        padding-right: 15px;
        position: fixed;
        top: 0;
        width: 100%;
    }
    .work__list {
        display: flex;
        flex-wrap: nowrap;
    }
}
</style>
