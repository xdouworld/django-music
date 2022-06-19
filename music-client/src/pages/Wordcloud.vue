<template>
    <div class="song-list">
        <ul class="song-list-header">
            <li v-for="(item,index) in ranking" :key="index" @click="handleChangeView(item.name)"
                :class="{active:item.name==activeName}">
                {{item.name}}
            </li>
        </ul>
        <img :src="imgurl" style="padding-left: 50px"></img>
    </div>
</template>
<script>
import {mapGetters} from "vuex";
import AlbumContent from "../components/AlbumContent";
import {getAllSongList,getrankingListOfLikeStyle} from '../api/index';
import {mixin} from "../mixins";
import {ranking} from '../assets/data/songList';


export default {
    name: 'song-list',
    mixins: [mixin],
    components:{
        AlbumContent,
 
    },
    data(){
        return{
            imgurl:'http://127.0.0.1:8000/static/test.png',
            currentPage: 1,      //当前页，默认第一页
            ranking: [],           //风格
            activeName: '飙升榜'    //当前风格
        }
    },
    computed:{
       ...mapGetters([
            'listOfSongs',      //当前播放列表
            'tempList',         //当前歌单对象
            'loginIn',          //用户是否已登录
            'userId',           //当前登录用户id
        ])
    },
    mounted(){
        this.ranking = ranking;
        this.getSongList();
    },

    methods:{
        getSongList(){            
            this.imgurl='http://127.0.0.1:8000/static/飙升榜.png'
        },
        //获取当前页
        handleCurrentChange(val){
            this.currentPage = val;
        },
        //根据style显示对应的歌单
        handleChangeView(name){
            this.activeName = name;
            console.log(name);
            this.imgurl='http://127.0.0.1:8000/static/'+name+'.png';
            console.log(this.imgurl);
            
        },
        //根据style查询对应的歌单
        goSongListOfStyle(style){
            getrankingListOfLikeStyle(style)
                .then(res =>{
                        this.currentPage = 1;
                        this.albumDatas = res;
                        this.songLists = res;
                        console.log(this.songLists);
                         this.$store.commit('setListOfSongs',this.songLists);
                    }) 
        },

    }
}


</script>

<style lang="scss" scoped>
@import '../assets/css/song-list.scss';
</style>
