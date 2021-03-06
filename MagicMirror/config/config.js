/* Magic Mirror Config Sample
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information how you can configurate this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */

var config = {
	address: "localhost", // Address to listen on, can be:
	                      // - "localhost", "127.0.0.1", "::1" to listen on loopback interface
	                      // - another specific IPv4/6 to listen on a specific interface
	                      // - "", "0.0.0.0", "::" to listen on any interface
	                      // Default, when address config is left out, is "localhost"
	port: 8080,
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], // Set [] to allow all IP addresses
	                                                       // or add a specific IPv4 of 192.168.1.5 :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
	                                                       // or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	language: "en",
	timeFormat: 12,
	units: "english",

	modules: [
		{
			module: "alert",
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "Upcoming Events",
			position: "top_left",
			config: {
				calendars: [
					{
						symbol: "calendar-check",
						url: "https://calendar.google.com/calendar/ical/hurl2471%40kettering.edu/private-8604eeef944ffd8edb8bfd51f82afc58/basic.ics",
						maximumNumberOfDays: "2"

						//url: 'http://www.calendarlabs.com/templates/ical/US-Holidays.ics',
						//symbol: 'calendar'
					}
						
				],

			}
		},
		{
			module: "compliments",
			position: "bottom_bar",
			config: {
				compliments: {
					anytime: [
						"Have a fantastic day!",
						"Time to start your day!",
						"Good morning, today is a wonderful day!"
					],
					morning: [
						"Good morning!",
						"Enjoy your day!",
						"Make something of yourself"
					],
					day_sunny: [
						"Today is a sunny day",
						"It's a beautiful day"
					],
					snow: [
						"Snowball battle!"
					],
					rain: [
						"Don't forget your umbrella"
					]
				}
			}
		},
		{
			module: "currentweather",
			position: "top_right",
			config: {
				location: "Flint city",
				locationID: "4062523",  //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				appid: "YOUR_OPENWEATHER_API_KEY"
			}
		},
		{
			module: "weatherforecast",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				location: "Flint city",
				locationID: "4062523",  //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				appid: "YOUR_OPENWEATHER_API_KEY"
			}
		},
		// {
		// 	module: "newsfeed",
		// 	position: "bottom_bar",
		// 	config: {
		// 		feeds: [
		// 			{
		// 				title: "New York Times",
		// 				url: "http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"
		// 			}
		// 		],
		// 		showSourceTitle: true,
		// 		showPublishDate: true,
		// 		broadcastNewsFeeds: true,
		// 		broadcastNewsUpdates: true
		// 	}
		// },

		//only shows what is playing have to set up raspoitfy on pi to actually play the music off the pi 
		// {
		//   module: "MMM-NowPlayingOnSpotify",
		//   position: "left",

		//   config: {
		//     clientID: "347a3344716b4e25b63f661462ffa0bd",
		//     clientSecret: "64178e8cb42b453bb720d8d404500c57",
		//     accessToken: "BQBqK720L7lmtVA3w0YabxPwFU77GkXwjFqss8b34e__ZBsOKwOF6Mp3wnsFo-wyjhIUdBDIhipgFiehhFH5NzEi4P1OKIGzY_ADjnYtdoNEOiErqkWGUtstXKZqvWVUby1sA1oPAVzmZCRheriDgzdM",
		//     refreshToken: "AQC5_ffePgMwZx3JdWR-6CPoPtn-butLdozcAWvsOeNxqd1djiotaW3Cr4POCx8AieVTHAXBHwa3uAl4eW9ENkiBX3Ex6WZlJMY-krlZIkGsk6SFG0JS_8e4BseUL72Nw9w"
		//   }
		// },

		    	{
		module: 'MMM-iFrame-Ping',
		// position: 'middle_center',	// This can be any of the regions.
		position: 'top_right',	// This can be any of the regions.
		config: {
			// See 'Configuration options' for more information.
			url: "https://www.youtube.com/embed/8sUOvDzmrks?autoplay=1&loop=1&playlist=8sUOvDzmrks", //url to display
			width:"1200px",
			autoRefresh: false, //set to false for video
			updateInterval: 1, //in min. Only if autoRefresh: true
			displayLastUpdate: true,
			height: "700px", //Optional. Default: 100px
			scrolling: "no"
			}
	},

	]

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
