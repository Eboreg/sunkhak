import Marionette from 'backbone.marionette';
import AppView from './views/AppView';
import PlaceCollection from './collections/PlaceCollection';

var Controller = Marionette.Object.extend({
    initialize: function() {
        this.options.regionManager = new Marionette.RegionManager({
            regions: {
                app: '#app',
            },
        });
        var initialData = this.getOption('initialData');
        var appview = new AppView({
            collection: new PlaceCollection(initialData.places),
        });
        this.getOption('regionManager').get('app').show(appview);
        this.options.appview = appview;
    },

    renderPlace : function(slug) {
        this.getOption('appview').triggerMethod('show:place', slug);
        this.setUpListeners();
    },
    renderInfo : function() {
        this.getParams();
        AppView.renderInfo(this.params);
        this.setUpListeners();
    },
    renderMap : function() {
        this.getParams();
        AppView.renderMap(this.params);
        this.setUpListeners();
    },

});

export default Controller;