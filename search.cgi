#!/usr/local/bin/perl

use strict;
use warnings;

use Lucy::Search::IndexSearcher;

my $term = shift || die "Usage: $0 search-term";

my $searcher = Lucy::Search::IndexSearcher->new( index => '/ppant/LucyTest/index');
# A basic search command line which will look for indexed items based on STDIN and will show that in which document query string is found and no of hits
my $hits = $searcher->hits( query => $term );
while ( my $hit = $hits->next ) {
        print "Title: $hit->{title} - ID: $hit->{id}\n";
}
# End of search.cgi