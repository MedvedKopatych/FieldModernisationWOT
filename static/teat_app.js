search_name = new Vue({
    el: '#search',
    data: {
        keyword: '',
        tanks:[],
    },
    methods: {
    getSearchName() {
        axios.get('/api/tanks_base/?search='+this.keyword)
        .then(response => (this.tanks = response.data))
        .catch(err => console.log(err));
        }
    },

}
)

new Vue({
  el: '#nation',
  data: {
    results: [],
    nations: NATIONS.split(', '), // create an array of the nations
    nation: '', // set default nation to ''
    loading: true,

  },

  methods: {
    getNation(nation) {
      axios.get('/api/tanks_base/?nation='+this.nation).then((response) => {
        this.loading = false;
        this.results = response.data.results;
      }).catch((error) => { console.log(error); });
    }
  }
});

new Vue({
  el: '#type',
  data: {
    results: [],
    types: TYPES.split(', '), // create an array of the types
    type: '', // set default  to ''
    loading: true,

  },

  methods: {
    getType(type) {
      axios.get('/api/tanks_base/?type='+this.type).then((response) => {
        this.loading = false;
        this.results = response.data.results;
      }).catch((error) => { console.log(error); });
    }
  }
});

new Vue({
  el: '#tier',
  data: {
    results: [],
    tiers: TIERS.split(', '), // create an array of the tiers
    tier: '', // set default  to ''
    loading: true,

  },

  methods: {
    getTier(tier) {
      axios.get('/api/tanks_base/?tier='+this.tier).then((response) => {
        this.loading = false;
        this.results = response.data.results;
      }).catch((error) => { console.log(error); });
    }
  }

watch: {
        keyword: function(event){
            if (event) {
                this.getSearchName(keyword);
            }
      }
     },