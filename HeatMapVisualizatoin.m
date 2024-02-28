% Read data from the text file
data = fileread('data.txt');

% Extract attacking dice, defending dice, and win percentage from the data
matches = regexp(data, 'With (\d+) attacking dice against (\d+) defending dice, the attackers win (\d+\.\d+)% of the time.', 'tokens');

% Convert the matches into numerical arrays
match_data = cellfun(@(x) str2double(x), vertcat(matches{:}));

% Create a sparse matrix to store win percentages
win_percentage_matrix = sparse(match_data(:,1), match_data(:,2), match_data(:,3));

% Generate a heatmap
heatmap(win_percentage_matrix, 'XLabel', 'Defending Dice', 'YLabel', 'Attacking Dice', 'ColorbarVisible', 'on', 'ColorMap', 'jet');
title('Win Percentage Heatmap');

% Set the axis to start from 1
xlim([0.5, 11.5]);
ylim([0.5, 10.5]);

% Invert y-axis to match the usual dice orientation
set(gca, 'YDir', 'reverse');
