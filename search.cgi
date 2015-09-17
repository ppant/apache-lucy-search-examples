#!/usr/local/bin/perl

use strict;
use warnings;

use Lucy::Search::IndexSearcher;

my $term = shift || die "Usage: $0 search-term";

my $searcher = Lucy::Search::IndexSearcher->new( index => '/pp/LucyTest/index');

my $hits = $searcher->hits( query => $term );
while ( my $hit = $hits->next ) {
        print "Title: $hit->{title} - ID: $hit->{id}\n";
}